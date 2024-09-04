# musicapp/urls.py
from django.contrib import admin
from django.urls import path
from .import views

from .views import artist_profile_view
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.dashboard_view, name='dashboard'),
    path('artist/<str:artist_id>/', artist_profile_view, name='artist_profile'),
    path('artists/', views.artists_view, name='artists'),
    path('artist/<str:artist_id>/', views.artist_detail_view, name='artist_detail'),
    path('track/<str:track_id>/', views.track_detail_view, name='track_detail'),
    #path('track/<str:track_id>/', views.track_detail_view, name='track_detail'),
    path('add_to_playlist/<str:track_id>/', views.add_to_playlist, name='add_to_playlist'),
    path('trending/', views.trending_music, name='trending_music'),
    path('videos/', views.video_list, name='video_list')
]