# Generated by Django 4.1.7 on 2023-05-05 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0013_rename_spaces_space'),
    ]

    operations = [
        migrations.AddField(
            model_name='space',
            name='master_space',
            field=models.IntegerField(null=True),
        ),
    ]
