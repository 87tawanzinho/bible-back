# Generated by Django 5.0.2 on 2024-03-04 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibleAuth', '0006_alter_profile_allchapters'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='devotionalWarn',
            field=models.BooleanField(default=False),
        ),
    ]