from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from jjltech.apps.pitchdeck.models import PitchDeck
from django.db.models import Q

def index_view(request):
    return render(request, 'core/website/index.html')
    
@login_required
def dashboard_view(request):

    user = request.user
    pitchdeck = PitchDeck.objects.filter(user=user).first()
    total_users = User.objects.count()
    same_country_users = User.objects.filter(profile__country=user.profile.country).count()
    same_industry_users = PitchDeck.objects.filter(industry=pitchdeck.industry).count() if pitchdeck else 0

    context = { 

        'user': user,
        'pitchdeck': pitchdeck,
        'total_users': total_users,
        'same_country_users': same_country_users,
        'same_industry_users': same_industry_users,
    }
    return render(request, 'core/dashboard.html', context)
