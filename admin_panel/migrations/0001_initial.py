# Generated by Django 4.1 on 2022-08-09 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciality', models.CharField(max_length=255)),
                ('discription', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Speciality',
            },
        ),
    ]
