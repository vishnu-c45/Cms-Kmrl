# Generated by Django 4.1.7 on 2023-05-19 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0036_invoices_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=225, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='invoices',
            name='taxable_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='invoices',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
