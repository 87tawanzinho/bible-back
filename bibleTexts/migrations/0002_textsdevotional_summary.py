# Generated by Django 5.0.2 on 2024-03-06 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibleTexts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textsdevotional',
            name='summary',
            field=models.CharField(default='13', max_length=400),
            preserve_default=False,
        ),
    ]