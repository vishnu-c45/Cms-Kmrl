# Generated by Django 4.1.7 on 2023-05-18 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0033_remove_invoices_customer_contact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoices',
            name='customer_contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.customer_contact'),
        ),
    ]
