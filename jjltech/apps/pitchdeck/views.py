from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import PitchDeck
from .forms import PitchDeckForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from django_countries import countries

# Options for Industry Choices
INDUSTRY_CHOICES = [
        ('tech', 'Technology'),
        ('finance', 'Finance'),
        ('health', 'Healthcare'),
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('retail', 'Retail'),
        ('manufacturing', 'Manufacturing'),
        ('real_estate', 'Real Estate'),
        ('transportation', 'Transportation'),
        ('energy', 'Energy'),
        ('agriculture', 'Agriculture'),
        ('hospitality', 'Hospitality'),
        ('construction', 'Construction'),
        ('legal', 'Legal'),
        ('marketing', 'Marketing'),
        ('media', 'Media'),
        ('non_profit', 'Non-Profit'),
        ('sports', 'Sports'),
        ('telecommunications', 'Telecommunications'),
        ('utilities', 'Utilities'),
        ('other', 'Other'),
    ]


def create_pitch_view(request):
    if request.method == 'POST':
        form = PitchDeckForm(request.POST)
        if form.is_valid():
            pitch = form.save(commit=False)
            pitch.user = request.user
            pitch.save()
            return redirect('pitchdeck:detail')
    else:
        form = PitchDeckForm()
    return render(request, 'pitchdeck/create.html', {'form': form})

def edit_pitch_view(request):
    user = request.user
    pitch = PitchDeck.objects.filter(user=user).first()
    if request.method == 'POST':
        form = PitchDeckForm(request.POST, instance=pitch)
        if form.is_valid():
            pitch = form.save(commit=False)
            pitch.user = request.user
            pitch.save()
            return redirect('pitchdeck:detail')
    else:
        form = PitchDeckForm(instance=pitch)
    return render(request, 'pitchdeck/edit.html', {'form': form})

def pitchdeck_detail_view(request):
    user = request.user
    pitch = PitchDeck.objects.filter(user=user).first()
    return render(request, 'pitchdeck/detail.html', {'pitch': pitch})

def pitchdeck_board(request):
    # get country choices from the country fields module
    country_choices = countries
    # get industry choices from the PitchDeck model
    industry_choices = INDUSTRY_CHOICES
    pitchdecks = PitchDeck.objects.all()
    # get top pitches, pitches with highest likes
    top_pitches = pitchdecks.order_by('-likes')[:5]
    industry = request.GET.get('industry')
    country = request.GET.get('country')
    keywords = request.GET.get('keywords')

    if industry:
        pitchdecks = pitchdecks.filter(industry=industry)
    if country:
        pitchdecks = pitchdecks.filter(user__profile__country=country)
    if keywords:
        pitchdecks = pitchdecks.filter(
            Q(pitch__icontains=keywords)
        )

    # Paginate the pitchdecks
    paginator = Paginator(pitchdecks, 12)  # Show 12 pitches per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'country_choices': country_choices,
        'industry_choices': industry_choices,
        'top_pitches': top_pitches,
        'industry': industry,
        'country': country,
        'keywords': keywords,
    }
    return render(request, 'pitchdeck/pitchdeck_board.html', context)


def like_pitch(request, pitch_id):
    pitch = get_object_or_404(PitchDeck, id=pitch_id)
    if request.user in pitch.likes.all():
        pitch.likes.remove(request.user)
        liked = False
    else:
        pitch.likes.add(request.user)
        liked = True
    return JsonResponse({'liked': liked, 'likes_count': pitch.likes.count()})


def pitchdeck_view(request, pitch_id):
    pitch = get_object_or_404(PitchDeck, id=pitch_id)
    pitch.clicks += 1
    pitch.save()

    # Fetch similar pitches based on industry or country
    similar_pitches = PitchDeck.objects.filter(
        Q(industry=pitch.industry) | Q(user__profile__country=pitch.user.profile.country)
    ).exclude(id=pitch.id)[:5]  # Exclude the current pitch and limit to 5

    context = {
        'pitch': pitch,
        'similar_pitches': similar_pitches,
    }
    return render(request, 'pitchdeck/pitchdeck.html', context)