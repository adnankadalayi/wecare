# Generated by Django 4.1 on 2022-08-09 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_panel', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE')], max_length=10)),
                ('degree', models.CharField(max_length=255)),
                ('experience', models.IntegerField()),
                ('registration_no', models.IntegerField()),
                ('state_medical_council', models.CharField(max_length=255)),
                ('address', models.TextField(max_length=255)),
                ('medical_speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.speciality')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
