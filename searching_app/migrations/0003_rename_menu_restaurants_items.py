# Generated by Django 4.2.2 on 2023-06-26 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searching_app', '0002_rename_restaurants_id_restaurants_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurants',
            old_name='menu',
            new_name='items',
        ),
    ]
