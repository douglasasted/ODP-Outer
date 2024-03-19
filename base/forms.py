from django.forms import ModelForm
from .models import Character, Campaign

class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = [
            'name', 
            'classe', 
            'origin',
            'attribute_agility', 
            'attribute_strength', 
            'attribute_intellect', 
            'attribute_vigor', 
            'attribute_presence',
            'appearance',
            'personality',
            'background',
            'objective']

class CampaignForm(ModelForm):
    class Meta:
        model = Campaign
        fields = '__all__'