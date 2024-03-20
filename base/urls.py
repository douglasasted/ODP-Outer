from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),

    path('characters/', views.characters, name='characters'),
    path('character/<str:pk>/', views.character, name='character'),
    path('create-character/', views.createCharacter, name='create-character'),
    path('delete-character/<str:pk>/', views.deleteCharacter, name='delete-character'),

    path('campaigns/', views.campaigns, name='campaigns'),
    path('campaign/<str:pk>/', views.campaign, name='campaign'),
    path('create-campaign/', views.createCampaign, name='create-campaign'),
    path('delete-campaign/<str:pk>/', views.deleteCampaign, name='delete-campaign'),
    path('update-campaign/<str:pk>/', views.updateCampaign, name='update-campaign')
]