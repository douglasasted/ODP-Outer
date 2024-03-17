from django.shortcuts import render
from .models import Character

def about(request):
    return render(request, 'base/about.html')

def characters(request):
    _characters = Character.objects.all()

    context = {'characters': _characters}
    return render(request, 'base/characters.html', context)

def campaigns(request):
    return render(request, 'base/campaigns.html')

def character(request, pk):
    character = Character.objects.get(id=pk)

    context = {'character': character}
    return render(request, 'base/character.html', context)