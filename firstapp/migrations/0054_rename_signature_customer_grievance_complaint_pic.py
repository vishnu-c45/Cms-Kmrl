# Generated by Django 4.1.7 on 2023-05-24 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0053_customer_grievance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer_grievance',
            old_name='signature',
            new_name='complaint_pic',
        ),
    ]
