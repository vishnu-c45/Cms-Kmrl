# Generated by Django 4.1.7 on 2023-05-24 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0055_alter_customer_grievance_complaint_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_grievance',
            name='complaint_pic',
            field=models.FileField(blank=True, default='null', null=True, upload_to='media/uploadedimages/'),
        ),
    ]
