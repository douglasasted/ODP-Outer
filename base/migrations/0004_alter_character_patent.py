# Generated by Django 5.0.3 on 2024-03-19 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_character_appearance_character_attribute_agility_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='patent',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
