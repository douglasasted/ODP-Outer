# Generated by Django 5.0.3 on 2024-04-10 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_rename_rituals_ritual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='patent',
            field=models.IntegerField(blank=True, max_length=200, null=True),
        ),
    ]
