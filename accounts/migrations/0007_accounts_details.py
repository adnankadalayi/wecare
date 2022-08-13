# Generated by Django 4.1 on 2022-08-09 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_alter_doctor_detail_medical_speciality'),
        ('accounts', '0006_remove_accounts_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='details',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctors.doctor_detail'),
        ),
    ]
