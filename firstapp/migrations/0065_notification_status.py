# Generated by Django 4.2 on 2023-06-01 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0064_notification_alter_login_table_phno_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='status',
            field=models.IntegerField(null=True),
        ),
    ]
