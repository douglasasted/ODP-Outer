# Generated by Django 5.0.3 on 2024-03-20 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_origiin_character_origin'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]