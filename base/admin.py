from django.contrib import admin

# Register your models here.

from .models import Character, Campaign

admin.site.register(Character)
admin.site.register(Campaign)