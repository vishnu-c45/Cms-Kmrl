# Generated by Django 4.2 on 2023-06-01 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0065_notification_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='type',
            field=models.IntegerField(null=True),
        ),
    ]
