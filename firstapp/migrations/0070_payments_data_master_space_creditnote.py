# Generated by Django 4.1.7 on 2023-06-06 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0069_remove_payments_data_payment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments_data',
            name='master_space',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.space'),
        ),
        migrations.CreateModel(
            name='CreditNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_note_number', models.CharField(max_length=50, unique=True)),
                ('date', models.DateField()),
                ('reference_invoice_number', models.CharField(max_length=50)),
                ('reference_invoice_date', models.DateField()),
                ('reason', models.TextField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('terms_and_conditions', models.TextField()),
                ('contact_info', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credit_notes', to='firstapp.customer_contact')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.invoices')),
            ],
        ),
    ]
