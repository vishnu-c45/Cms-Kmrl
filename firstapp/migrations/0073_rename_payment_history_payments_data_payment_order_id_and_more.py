# Generated by Django 4.1.7 on 2023-06-15 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0072_customer_contact_password_customer_contact_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payments_data',
            old_name='payment_history',
            new_name='payment_order_id',
        ),
        migrations.AddField(
            model_name='payments_data',
            name='payment_signature',
            field=models.CharField(max_length=225, null=True),
        ),
    ]
