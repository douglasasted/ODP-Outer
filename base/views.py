from django.shortcuts import render, redirect
from .models import Character
from .forms import CharacterForm

def about(request):
    return render(request, 'base/about.html')

def campaigns(request):
    return render(request, 'base/campaigns.html')


def characters(request):
    _characters = Character.objects.all()

    context = {'characters': _characters}
    return render(request, 'base/characters.html', context)

def character(request, pk):
    character = Character.objects.get(id=pk)

    context = {'character': character}
    return render(request, 'base/character.html', context)

def createCharacter(request):
    form = CharacterForm()
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('characters')

    context = {'form': form}
    return render(request, 'base/character_form.html', context)