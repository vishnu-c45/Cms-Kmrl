# Generated by Django 4.1.7 on 2023-05-24 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0052_alter_company_details_signature'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_grievance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', models.FileField(blank=True, default='', null=True, upload_to='media/uploadedimages/')),
                ('reason', models.CharField(max_length=225, null=True)),
                ('complaint', models.CharField(max_length=225, null=True)),
                ('status', models.IntegerField(null=True)),
                ('created_on', models.DateTimeField(null=True)),
                ('updated_on', models.DateTimeField(null=True)),
                ('updated_by', models.IntegerField(null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.login_table')),
                ('customer_contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.customer_contact')),
                ('master_space', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.space')),
            ],
        ),
    ]
