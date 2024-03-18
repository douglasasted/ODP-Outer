from django.db import models

class Character(models.Model):
    # user = a
    # campaign = 
    name = models.CharField(max_length=200)
    classe = models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Campaign(models.Model):
    # master = 
    # users = 
    name = models.CharField(max_length=200)
    
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

