# Generated by Django 4.1.7 on 2023-03-30 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.BigIntegerField(null=True),
        ),
    ]
