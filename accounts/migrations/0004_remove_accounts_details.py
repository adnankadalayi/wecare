# Generated by Django 4.1 on 2022-08-09 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_accounts_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='details',
        ),
    ]
