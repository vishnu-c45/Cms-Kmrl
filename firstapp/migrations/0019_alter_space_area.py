# Generated by Django 4.1.7 on 2023-05-08 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0018_merge_20230508_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='area',
            field=models.BigIntegerField(null=True),
        ),
    ]
