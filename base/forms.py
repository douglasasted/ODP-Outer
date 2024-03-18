from django.forms import ModelForm
from .models import Character, Campaign

class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = '__all__'

class CampaignForm(ModelForm):
    class Meta:
        model = Campaign
        fields = '__all__'