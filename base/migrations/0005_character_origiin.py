# Generated by Django 5.0.3 on 2024-03-19 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_character_patent'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='origiin',
            field=models.CharField(default='Mercenary', max_length=200),
            preserve_default=False,
        ),
    ]