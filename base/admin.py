from django.contrib import admin

# Register your models here.

from .models import Character, Campaign, Message, Ability, Ritual, GeneralItem, WeaponItem, ProtectionItem, CursedItem

admin.site.register(Character)
admin.site.register(Campaign)
admin.site.register(Message)

admin.site.register(Ability)
admin.site.register(Ritual)
admin.site.register(GeneralItem)
admin.site.register(WeaponItem)
admin.site.register(ProtectionItem)
admin.site.register(CursedItem)