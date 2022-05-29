# Generated by Django 4.0.3 on 2022-05-29 07:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_account_first_name_alter_account_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[A-Za-z][A-Za-z ]*$', 'Enter a valid name')]),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[A-Za-z][A-Za-z ]*$', 'Enter a valid name')]),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$')]),
        ),
    ]
