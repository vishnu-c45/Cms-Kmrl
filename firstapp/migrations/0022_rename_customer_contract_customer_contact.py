# Generated by Django 4.2 on 2023-05-15 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0021_alter_contract_customer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='customer',
            new_name='customer_contact',
        ),
    ]
