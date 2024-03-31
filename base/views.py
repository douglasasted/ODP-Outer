from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Character, Campaign, Message
from .forms import CharacterForm, CampaignForm
from django.http import HttpResponse, JsonResponse
import math


# General Information

# Get all skills in a single array
skills = []
fields = Character._meta.get_fields()
for field in fields:
    if field.name[:5] == "skill":
        skills.append(field.name)

skill_count = math.floor(len(skills) / 3)



def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('about')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('about')
        else:
            messages.error(request, 'Username OR password does not exist')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('about')


def registerUser(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            user.username = user.username.lower()
            user.save()

            login(request, user)

            return render(request, 'base/about.html')
        else:
            messages.error(request, 'An error occurred during registration')

    context = {'form': form}
    return render(request, 'base/login_register.html', context)


@login_required(login_url='login')
def profile(request):
    return render(request, 'base/profile.html')


def sendMessage(request):
    campaign = Campaign.objects.get(id=request.POST['campaign'])
    body = request.POST['body']

    message = Message.objects.create(user=request.user, username=request.user.username, campaign=campaign, body=body)
    message.save()

    return HttpResponse('Message sent successfully')

def getMessage(request, pk):
    campaign = Campaign.objects.get(name=pk)

    messages = Message.objects.filter(campaign=campaign.id)
    
    context = {'messages': list(messages.values()) }
    return JsonResponse(context)

def about(request):
    return render(request, 'base/about.html')



# ---------------------------
# Character: Creation & visualization
# ---------------------------
@login_required(login_url='login')
def characters(request):
    _characters = Character.objects.all()

    context = {'characters': _characters}
    return render(request, 'base/character/characters.html', context)


@login_required(login_url='login')
def character(request, pk):
    character = Character.objects.get(id=pk)

    context = {'character': character, 'skills': skills, 'skills_count': range(skill_count)}
    return render(request, 'base/character/character.html', context)


@login_required(login_url='login')
def createCharacter(request):
    form = CharacterForm()
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            final_form = form.save(commit=False)

            final_form.player = request.user
            final_form.save()

            return redirect('characters')

    context = {'form': form}
    return render(request, 'base/character/character_form.html', context)


@login_required(login_url='login')
def deleteCharacter(request, pk):
    character = Character.objects.get(id=pk)

    if request.user != character.player:
        return redirect('characters')

    if request.method == 'POST':
        character.delete()
        return redirect('characters')

    context = {'obj': character}
    return render(request, 'base/delete.html', context)


@login_required(login_url='login')
def updateCharacter(request, pk):
    character = Character.objects.get(id=pk)

    if request.user != character.player:
        return

    character.attribute_agility = request.POST['attribute_agility']
    character.attribute_strength = request.POST['attribute_strength']
    character.attribute_intellect = request.POST['attribute_intellect']
    character.attribute_vigor = request.POST['attribute_vigor']
    character.attribute_presence = request.POST['attribute_presence']

    character.current_health = request.POST['current_health']
    character.max_health = request.POST['max_health']
    character.current_sanity = request.POST['current_sanity']
    character.max_sanity = request.POST['max_sanity']
    character.current_effort = request.POST['current_effort']
    character.max_effort = request.POST['max_effort']

    character.classe = request.POST['classe']
    character.origin = request.POST['origin']
    
    character.paranormal_exposition = request.POST['paranormal_exposition']
    character.pe_turn = request.POST['pe_turn']
    character.speed = request.POST['speed']

    character.equipment_defense = request.POST['equipment_defense']
    character.other_defense = request.POST['other_defense']

    character.block = request.POST['block']
    character.dodge = request.POST['dodge']

    character.protection = request.POST['protection']
    character.resistance = request.POST['resistance']
    character.proficiency = request.POST['proficiency']
        
    for skill in skills:
        value = request.POST.get(skill, False)

        setattr(character, skill, value)

    character.notes = request.POST['notes']
    character.appearance = request.POST['appearance']
    character.personality = request.POST['personality']
    character.background = request.POST['background']
    character.objective = request.POST['objective']
    
    character.save()

    return HttpResponse('Character updated successfully')


# ---------------------------
# Campaign: Creation & visualization
# ---------------------------
@login_required(login_url='login')
def campaigns(request):
    campaigns = Campaign.objects.all()

    context = {'campaigns': campaigns}
    return render(request, 'base/campaign/campaigns.html', context)


@login_required(login_url='login')
def campaign(request, pk):
    campaign = Campaign.objects.get(id=pk)
    campaign_messages = campaign.message_set.all().order_by('created')
    participants = campaign.participants.all()

    context = {'campaign': campaign, 'campaign_messages': campaign_messages, 'participants': participants}
    return render(request, 'base/campaign/campaign.html', context)


@login_required(login_url='login')
def createCampaign(request):
    form = CampaignForm()
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        
        if form.is_valid():
            final_form = form.save(commit=False)

            final_form.owner = request.user
            final_form.save()

            return redirect('campaigns')
        
    context = {'form': form}
    return render(request, 'base/campaign/campaign_form.html', context)


@login_required(login_url='login')
def deleteCampaign(request, pk):
    campaign = Campaign.objects.get(id=pk)

    if request.user != campaign.owner:
        return redirect('campaigns')

    if request.method == 'POST':
        campaign.delete()
        return redirect('campaigns')

    context = {'obj': campaign}
    return render(request, 'base/delete.html', context)


@login_required(login_url='login')
def updateCampaign(request, pk):
    campaign = Campaign.objects.get(id=pk)
    form = CampaignForm(instance=campaign)

    if request.user != campaign.owner:
        return redirect('campaigns')

    if request.method == 'POST':
        form = CampaignForm(request.POST, instance=campaign)
        if form.is_valid():
            form.save()
            return redirect('campaign', pk)
        
    context = {'form': form}
    return render(request, 'base/campaign/campaign_form.html', context)