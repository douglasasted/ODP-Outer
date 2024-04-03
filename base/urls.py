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
    path('create-character/', views.createCharacter, name='create-character'),
    path('delete-character/<str:pk>/', views.deleteCharacter, name='delete-character'),
    path('character/<str:pk>/', views.character, name='character'),
    path('character-update/<str:pk>/', views.updateCharacter, name='update-character'),
    
    path('add-ability/', views.addAbility, name='add-ability'),
    path('delete-ability/', views.deleteAbility, name='delete-ability'),
    path('update-ability/', views.updateAbility, name='update-ability'),
    #path('add-ritual/', views.addRitual, name='add-ritual'),
    #path('delete-ritual/', views.deleteRitual, name='delete-ritual'),
    #path('update-ritual/', views.updateRitual, name='update-ritual'),
    #path('add-item/', views.addItem, name='add-item'),
    #path('delete-item/', views.deleteItem, name='delete-item'),
    #path('update-item/', views.updateItem, name='update-item'),

    path('campaigns/', views.campaigns, name='campaigns'),
    path('create-campaign/', views.createCampaign, name='create-campaign'),
    path('delete-campaign/<str:pk>/', views.deleteCampaign, name='delete-campaign'),
    path('campaign/<str:pk>/', views.campaign, name='campaign'),
    path('campaign-update/<str:pk>/', views.updateCampaign, name='update-campaign'),
    path('campaign-share/<str:pk>/', views.shareCampaign, name='share-campaign'),
    path('campaign-enter/<str:pk>/', views.enterCampaign, name='enter-campaign'),
    path('campaign-remove-player/', views.removePlayerCampaign, name='remove-player-campaign'),
    path('campaign-add-character/<str:pk>/', views.addCharacterCampaign, name='add-character-campaign'),
    path('campaign-remove-character/', views.removeCharacterCampaign, name='remove-character-campaign')
]