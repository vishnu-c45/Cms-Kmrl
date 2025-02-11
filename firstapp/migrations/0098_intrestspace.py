# Generated by Django 5.0.1 on 2024-02-21 12:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0097_alter_utility_status_alter_utility_water'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntrestSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField(null=True)),
                ('login_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.login_table')),
                ('space_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.space')),
            ],
        ),
    ]
