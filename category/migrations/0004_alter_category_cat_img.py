# Generated by Django 4.0.3 on 2022-05-29 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_remove_category_status_remove_category_trending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_img',
            field=models.ImageField(upload_to='photos/category'),
        ),
    ]
