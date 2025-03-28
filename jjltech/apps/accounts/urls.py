# Urls.py file for accounts app
from django.urls import path
from .views import login_view, logout_view, home_view, sign_up, view_profile, edit_profile

app_name = 'accounts'
urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('sign_up/', sign_up, name='signup'),
    path('profile/', view_profile, name='view_profile'),
    path('profile/edit/', edit_profile, name='edit_profile')
]