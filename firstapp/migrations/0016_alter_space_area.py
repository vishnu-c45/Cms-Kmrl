# Generated by Django 4.2 on 2023-05-06 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0015_alter_space_master_space'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='area',
            field=models.IntegerField(null=True),
        ),
    ]
