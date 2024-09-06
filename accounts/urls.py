from django.urls import path
from .views import SignUpView, edit_profile, artist_profile_view, artists_view, artist_detail_view, track_detail_view, add_to_playlist, trending_music, video_list, dashboard_view
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    path("", SignUpView.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(), name="logout"),  # Changed to Django's built-in LogoutView
    path("edit/", edit_profile, name="edit_profile"),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('artist/<str:artist_id>/', artist_profile_view, name='artist_profile'),
    path('artists/', artists_view, name='artists'),
    path('artist/<str:artist_id>/', artist_detail_view, name='artist_detail'),  # Potential conflict here
    path('track/<str:track_id>/', track_detail_view, name='track_detail'),
    path('add_to_playlist/<str:track_id>/', add_to_playlist, name='add_to_playlist'),
    path('trending/', trending_music, name='trending_music'),
    path('videos/', video_list, name='video_list'),
    path("profile/", views.profile, name="profile"),
    path("downloads/", views.downloads, name="downloads"),
    path("albums/", views.albums, name="albums"),
    path("playlists/", views.playlists, name="playlists"),
    path("favorites/", views.favorites, name="favorites"),
]
