# Generated by Django 2.2.7 on 2019-11-13 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20191113_1433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='hashtag',
            new_name='hashtags',
        ),
    ]
