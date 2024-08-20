from django.urls import path
from . import views


urlpatterns = [
    path("", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('edit_profile/<int:id>', views.edit_profile, name='edit_profile'),
    path('downloads/', views.downloads, name='downloads'),
    path('albums/', views.albums, name='albums'),
    path('playlists/', views.playlists, name='playlists'),
    path('favorites/', views.favorites, name='favorites'),
   
]
