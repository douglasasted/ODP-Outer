from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('characters/', views.characters, name='characters'),
    path('campaigns/', views.campaigns, name='campaigns'),
    path('character/<str:pk>/', views.character, name='character')
]