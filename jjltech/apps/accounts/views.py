# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import LoginForm, SignUpForm, ProfileForm
from .models import Profile


def home_view(request):
    return HttpResponseRedirect(reverse('accounts:login'))

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("core:dashboard")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})

def logout_view(request):
    logout(request)
    return redirect('accounts:login')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()

            # Create the profile
            Profile.objects.create(
                user=user,
                country=form.cleaned_data.get('country'),
                headline=form.cleaned_data.get('headline'),
                bio=form.cleaned_data.get('bio'),
            )

            messages.success(request, 'Kindly Login to your Account.')
            return redirect('accounts:login')
        else:
            messages.error(request, 'There was an error creating the user.')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


@login_required
def view_profile(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'accounts/view_profile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:view_profile')
    else:
        form = ProfileForm(instance=request.user.profile)

    context = {
        'form': form,
    }
    return render(request, 'accounts/edit_profile.html', context)