# Generated by Django 4.2 on 2023-05-08 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0016_alter_space_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='metrostation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.metrostationcontact'),
        ),
    ]
