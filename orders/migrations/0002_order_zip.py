# Generated by Django 4.0.3 on 2022-04-20 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='zip',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
