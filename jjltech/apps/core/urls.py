from django.urls import path
from .views import dashboard_view, index_view


app_name = 'core'

urlpatterns = [
    path('', index_view, name='index'),
    path('dashboard/', dashboard_view, name='dashboard'),

   
]
