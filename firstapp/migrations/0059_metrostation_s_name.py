# Generated by Django 4.1.7 on 2023-05-25 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0058_customer_grievance_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='metrostation',
            name='s_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
