# Generated by Django 5.1.4 on 2024-12-28 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniapp', '0002_quest_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quest',
            name='description',
        ),
    ]
