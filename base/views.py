from django.shortcuts import render, redirect
from .models import Character, Campaign
from .forms import CharacterForm, CampaignForm

def about(request):
    return render(request, 'base/about.html')


# Character: Creation & visualization
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

def deleteCharacter(request, pk):
    character = Character.objects.get(id=pk)

    if request.method == 'POST':
        character.delete()
        return redirect('characters')

    context = {'obj': character}
    return render(request, 'base/delete.html', context)


# Campaign: Creation & visualization
def campaigns(request):
    campaigns = Campaign.objects.all()

    context = {'campaigns': campaigns}
    return render(request, 'base/campaigns.html', context)

def campaign(request, pk):
    campaign = Campaign.objects.get(id=pk)

    context = {'campaign': campaign}
    return render(request, 'base/campaign.html', context)

def createCampaign(request):
    form = CampaignForm()
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('campaigns')
        
    context = {'form': form}
    return render(request, 'base/campaign_form.html', context)

def deleteCampaign(request, pk):
    campaign = Campaign.objects.get(id=pk)

    if request.method == 'POST':
        campaign.delete()
        return redirect('campaigns')

    context = {'obj': campaign}
    return render(request, 'base/delete.html', context)