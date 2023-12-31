# Generated by Django 4.2.2 on 2023-06-26 19:57

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('restaurants_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('menu', jsonfield.fields.JSONField(default=dict)),
            ],
        ),
    ]
