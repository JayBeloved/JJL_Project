from django.urls import path
from .views import create_pitch_view, edit_pitch_view, pitchdeck_detail_view, pitchdeck_board 
from .views import like_pitch, pitchdeck_view

app_name = 'pitchdeck'

urlpatterns = [
    path('create/', create_pitch_view, name='create'),
    path('edit/', edit_pitch_view, name='edit'),
    path('detail/', pitchdeck_detail_view, name='detail'),
    path('board/', pitchdeck_board, name='board'),
    path('like/<int:pitch_id>/', like_pitch, name='like_pitch'),
    path('view/<int:pitch_id>/', pitchdeck_view, name='pitchdeck_view')
]
