from django.contrib import admin

# Register your models here.

from .models import Character, Campaign, Message

admin.site.register(Character)
admin.site.register(Campaign)
admin.site.register(Message)