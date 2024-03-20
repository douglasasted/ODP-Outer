from django.db import models

class Character(models.Model):
    # player =   
    # campaign = 
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

    #attacks
    #abilities
    #inventory
    #rituals

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
    skill_animal_handling = models.IntegerField(default=0)
    skill_animal_handling_others = models.IntegerField(default=0)
    skill_art = models.IntegerField(default=0)
    skill_art_others = models.IntegerField(default=0)
    skill_athletics = models.IntegerField(default=0)
    skill_athletics_others = models.IntegerField(default=0)
    skill_current_times = models.IntegerField(default=0)
    skill_current_times_others = models.IntegerField(default=0)
    skill_science = models.IntegerField(default=0)
    skill_science_others = models.IntegerField(default=0)
    skill_crime = models.IntegerField(default=0)
    skill_crime_others = models.IntegerField(default=0)
    skill_diplomacy = models.IntegerField(default=0)
    skill_diplomacy_others = models.IntegerField(default=0)
    skill_deception = models.IntegerField(default=0)
    skill_deception_others = models.IntegerField(default=0)
    skill_fortitude = models.IntegerField(default=0)
    skill_fortitude_others = models.IntegerField(default=0)
    skill_stealth = models.IntegerField(default=0)
    skill_stealth_others = models.IntegerField(default=0)
    skill_initiative = models.IntegerField(default=0)
    skill_initiative_others = models.IntegerField(default=0)
    skill_intimidation = models.IntegerField(default=0)
    skill_intimidation_others = models.IntegerField(default=0)
    skill_insight = models.IntegerField(default=0)
    skill_insight_others = models.IntegerField(default=0)
    skill_investigation = models.IntegerField(default=0)
    skill_investigation_others = models.IntegerField(default=0)
    skill_melee = models.IntegerField(default=0)
    skill_melee_others = models.IntegerField(default=0)
    skill_medicine = models.IntegerField(default=0)
    skill_medicine_others = models.IntegerField(default=0)
    skill_occultism = models.IntegerField(default=0)
    skill_occultism_others = models.IntegerField(default=0)
    skill_perception = models.IntegerField(default=0)
    skill_perception_others = models.IntegerField(default=0)
    skill_driving = models.IntegerField(default=0)
    skill_driving_others = models.IntegerField(default=0)
    skill_aim = models.IntegerField(default=0)
    skill_aim_others = models.IntegerField(default=0)
    skill_profession = models.IntegerField(default=0)
    skill_profession_others = models.IntegerField(default=0)
    skill_reflex = models.IntegerField(default=0)
    skill_reflex_others = models.IntegerField(default=0)
    skill_religion = models.IntegerField(default=0)
    skill_religion_others = models.IntegerField(default=0)
    skill_survival = models.IntegerField(default=0)
    skill_survival_others = models.IntegerField(default=0)
    skill_tactics = models.IntegerField(default=0)
    skill_tactics_others = models.IntegerField(default=0)
    skill_technology = models.IntegerField(default=0)
    skill_technology_others = models.IntegerField(default=0)
    skill_will = models.IntegerField(default=0)
    skill_will_others = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Campaign(models.Model):
    # master = 
    # users = 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

