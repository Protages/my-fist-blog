# Generated by Django 3.2.7 on 2021-10-06 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0004_cat_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='image',
            field=models.ImageField(upload_to='img/'),
        ),
    ]