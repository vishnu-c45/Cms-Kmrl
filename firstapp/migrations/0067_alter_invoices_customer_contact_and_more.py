# Generated by Django 4.1.7 on 2023-06-02 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0066_notification_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoices',
            name='customer_contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='firstapp.customer_contact'),
        ),
        migrations.AlterField(
            model_name='payments_data',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payments_data', to='firstapp.customer_contact'),
        ),
    ]
