from django.db import models
from django.contrib.auth.models import User

class Character(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)  
    name = models.CharField(max_length=200)
    classe = models.CharField(max_length=200)
    origin = models.CharField(max_length=200)

    attribute_agility = models.IntegerField(default=1)
    attribute_strength = models.IntegerField(default=1)
    attribute_intellect = models.IntegerField(default=1)
    attribute_presence = models.IntegerField(default=1)
    attribute_vigor = models.IntegerField(default=1)

    paranormal_exposition = models.IntegerField(default=5)
    pe_turn = models.IntegerField(default=1)
    speed = models.IntegerField(default=9)

    current_health = models.IntegerField(default=0)
    max_health = models.IntegerField(default=0)
    current_sanity = models.IntegerField(default=0)
    max_sanity = models.IntegerField(default=0)
    current_effort = models.IntegerField(default=0)
    max_effort = models.IntegerField(default=0)

    equipment_defense = models.IntegerField(default=0)
    other_defense = models.IntegerField(default=0)

    block = models.IntegerField(default=0)
    dodge = models.IntegerField(default=0)

    protection = models.TextField(null=True, blank=True)
    resistance = models.TextField(null=True, blank=True)
    proficiency = models.TextField(null=True, blank=True)

    notes = models.TextField(null=True, blank=True)
    appearance = models.TextField(null=True, blank=True)
    personality = models.TextField(null=True, blank=True)
    background = models.TextField(null=True, blank=True)
    objective = models.TextField(null=True, blank=True)

    prestige = models.IntegerField(default=0)
    patent = models.CharField(null=True, blank=True, max_length=200)
    category_limit_1 = models.IntegerField(default=0)
    category_limit_2 = models.IntegerField(default=0)
    category_limit_3 = models.IntegerField(default=0)
    category_limit_4 = models.IntegerField(default=0)
    category_items_1 = models.IntegerField(default=0)
    category_items_2 = models.IntegerField(default=0)
    category_items_3 = models.IntegerField(default=0)
    category_items_4 = models.IntegerField(default=0)
    credit_limit = models.IntegerField(default=0)
    current_weight = models.IntegerField(default=0)
    max_weight = models.IntegerField(default=0)

    rituals_dc = models.IntegerField(default=0)

    skill_acrobacy = models.IntegerField(default=0)
    skill_acrobacy_others = models.IntegerField(default=0)
    skill_acrobacy_attribute = models.IntegerField(default=0)
    skill_animal_handling = models.IntegerField(default=0)
    skill_animal_handling_others = models.IntegerField(default=0)
    skill_animal_handling_attribute = models.IntegerField(default=3)
    skill_art = models.IntegerField(default=0)
    skill_art_others = models.IntegerField(default=0)
    skill_art_attribute = models.IntegerField(default=3)
    skill_athletics = models.IntegerField(default=0)
    skill_athletics_others = models.IntegerField(default=0)
    skill_athletics_attribute = models.IntegerField(default=4)
    skill_current_times = models.IntegerField(default=0)
    skill_current_times_others = models.IntegerField(default=0)
    skill_current_times_attribute = models.IntegerField(default=1)
    skill_science = models.IntegerField(default=0)
    skill_science_others = models.IntegerField(default=0)
    skill_science_attribute = models.IntegerField(default=1)
    skill_crime = models.IntegerField(default=0)
    skill_crime_others = models.IntegerField(default=0)
    skill_crime_attribute = models.IntegerField(default=0)
    skill_diplomacy = models.IntegerField(default=0)
    skill_diplomacy_others = models.IntegerField(default=0)
    skill_diplomacy_attribute = models.IntegerField(default=3)
    skill_deception = models.IntegerField(default=0)
    skill_deception_others = models.IntegerField(default=0)
    skill_deception_attribute = models.IntegerField(default=3)
    skill_fortitude = models.IntegerField(default=0)
    skill_fortitude_others = models.IntegerField(default=0)
    skill_fortitude_attribute = models.IntegerField(default=2)
    skill_stealth = models.IntegerField(default=0)
    skill_stealth_others = models.IntegerField(default=0)
    skill_stealth_attribute = models.IntegerField(default=0)
    skill_initiative = models.IntegerField(default=0)
    skill_initiative_others = models.IntegerField(default=0)
    skill_intiative_attribute = models.IntegerField(default=0)
    skill_intimidation = models.IntegerField(default=0)
    skill_intimidation_others = models.IntegerField(default=0)
    skill_intimidation_attribute = models.IntegerField(default=3)
    skill_insight = models.IntegerField(default=0)
    skill_insight_others = models.IntegerField(default=0)
    skill_insight_attribute = models.IntegerField(default=3)
    skill_investigation = models.IntegerField(default=0)
    skill_investigation_others = models.IntegerField(default=0)
    skill_investigation_attribute = models.IntegerField(default=1)
    skill_melee = models.IntegerField(default=0)
    skill_melee_others = models.IntegerField(default=0)
    skill_melee_attribute = models.IntegerField(default=4)
    skill_medicine = models.IntegerField(default=0)
    skill_medicine_others = models.IntegerField(default=0)
    skill_medicine_attribute = models.IntegerField(default=1)
    skill_occultism = models.IntegerField(default=0)
    skill_occultism_others = models.IntegerField(default=0)
    skill_occultism_attribute = models.IntegerField(default=1)
    skill_perception = models.IntegerField(default=0)
    skill_perception_others = models.IntegerField(default=0)
    skill_perception_attribute = models.IntegerField(default=3)
    skill_driving = models.IntegerField(default=0)
    skill_driving_others = models.IntegerField(default=0)
    skill_driving_attribute = models.IntegerField(default=0)
    skill_aim = models.IntegerField(default=0)
    skill_aim_others = models.IntegerField(default=0)
    skill_aim_attribute = models.IntegerField(default=0)
    skill_profession = models.IntegerField(default=0)
    skill_profession_others = models.IntegerField(default=0)
    skill_profession_attribute = models.IntegerField(default=1)
    skill_reflex = models.IntegerField(default=0)
    skill_reflex_others = models.IntegerField(default=0)
    skill_reflex_attribute = models.IntegerField(default=0)
    skill_religion = models.IntegerField(default=0)
    skill_religion_others = models.IntegerField(default=0)
    skill_religion_attribute = models.IntegerField(default=3)
    skill_survival = models.IntegerField(default=0)
    skill_survival_others = models.IntegerField(default=0)
    skill_survival_attribute = models.IntegerField(default=1)
    skill_tactics = models.IntegerField(default=0)
    skill_tactics_others = models.IntegerField(default=0)
    skill_tactics_attribute = models.IntegerField(default=1)
    skill_technology = models.IntegerField(default=0)
    skill_technology_others = models.IntegerField(default=0)
    skill_technology_attribute = models.IntegerField(default=1)
    skill_will = models.IntegerField(default=0)
    skill_will_others = models.IntegerField(default=0)
    skill_will_attribute = models.IntegerField(default=3)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_skill_name(self, skills, skill):
        return skills[skill * 3]
    
    def get_skill_formatted_name(self, skills, skill):
        return skills[skill * 3][6:].replace('_', ' ').capitalize()
        
    def get_selected_skill(self, value, property, skills, skill):
        skill_attribute = getattr(self, skills[property + skill * 3])

        if property == 0:
            value *= 5

        if value == skill_attribute:
            return "selected"
        
        return ""
    
    def get_selected_exposition(self, value):
        if (value == self.paranormal_exposition):
            return "selected"
        
        return ""
    
    def get_skill_value(self, skills, property, skill):
        return getattr(self, skills[property + skill * 3])


class Campaign(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    characters = models.ManyToManyField(Character, related_name='characters', blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    username = models.TextField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    body = models.TextField()
    type = models.IntegerField(default=0)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
    

class Ability(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    

class Ritual(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    
    element = models.IntegerField(default=0)
    circle = models.IntegerField(default=1)
    
    execution_time = models.TextField()
    range = models.TextField()
    area = models.TextField(null=True, blank=True)
    duration = models.TextField(null=True, blank=True)
    effect = models.TextField(null=True, blank=True)
    resistance = models.TextField(null=True, blank=True)
    
    dices = models.TextField(null=True, blank=True)
    risen_dices = models.TextField(null=True, blank=True)
    true_dices = models.TextField(null=True, blank=True)


    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class Item(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    category = models.IntegerField(default=0)
    spaces = models.IntegerField(default=0)
    
    class Meta:
        abstract=True


class GeneralItem(Item):
    tag = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class WeaponItem(Item):
    proficiency = models.CharField(max_length=200)
    weapon_type = models.CharField(max_length=200)
    grip_type = models.CharField(max_length=200)

    damage = models.CharField(max_length=200, null=True, blank=True)
    secondary_damage = models.CharField(max_length=200, null=True, blank=True)
    critical = models.IntegerField(default=20)
    multiplier = models.IntegerField(default=2)
    damage_type = models.CharField(max_length=200)
    range = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ProtectionItem(Item):
    defense = models.IntegerField(default=1)
    
    def __str__(self):
        return self.name


class CursedItem(Item):
    element = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name