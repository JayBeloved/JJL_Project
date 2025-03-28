from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import PitchDeck
from .forms import PitchDeckForm
from django.db.models import Q


def create_pitch_view(request):
    if request.method == 'POST':
        form = PitchDeckForm(request.POST)
        if form.is_valid():
            pitch = form.save(commit=False)
            pitch.user = request.user
            pitch.save()
            return redirect('pitchdeck:detail', pk=pitch.pk)
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
            return redirect('pitchdeck:detail', pk=pitch.pk)
    else:
        form = PitchDeckForm(instance=pitch)
    return render(request, 'pitchdeck/edit.html', {'form': form})

def pitchdeck_detail_view(request):
    user = request.user
    pitch = PitchDeck.objects.filter(user=user).first()
    return render(request, 'pitchdeck/detail.html', {'pitch': pitch})

def pitchdeck_board(request):
    pitchdecks = PitchDeck.objects.all()
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

    context = {
        'pitchdecks': pitchdecks,
        'industry': industry,
        'country': country,
        'keywords': keywords,
    }
    return render(request, 'pitchdeck/pitchdeck_board.html', context)