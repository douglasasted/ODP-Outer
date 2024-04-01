from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('profile/', views.profile, name='profile'),
    
    path('send-message/', views.sendMessage, name='send-message'),
    path('get-message/<str:pk>/', views.getMessage, name='get-message'),


    path('', views.about, name='about'),

    path('characters/', views.characters, name='characters'),
    path('character/<str:pk>/', views.character, name='character'),
    path('create-character/', views.createCharacter, name='create-character'),
    path('delete-character/<str:pk>/', views.deleteCharacter, name='delete-character'),
    path('update-character/<str:pk>/', views.updateCharacter, name='update-character'),

    path('campaigns/', views.campaigns, name='campaigns'),
    path('campaign/<str:pk>/', views.campaign, name='campaign'),
    path('create-campaign/', views.createCampaign, name='create-campaign'),
    path('delete-campaign/<str:pk>/', views.deleteCampaign, name='delete-campaign'),
    path('update-campaign/<str:pk>/', views.updateCampaign, name='update-campaign'),
    path('share-campaign/<str:pk>/', views.shareCampaign, name='share-campaign'),
    path('enter-campaign/<str:pk>/', views.enterCampaign, name='enter-campaign'),
    path('remove-player-campaign/', views.removePlayerCampaign, name='remove-player-campaign')
]