# Generated by Django 5.0.2 on 2024-03-05 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibleTexts', '0002_remove_textsdevotional_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='textsdevotional',
            name='summary',
            field=models.CharField(default='kk', max_length=400),
            preserve_default=False,
        ),
    ]
