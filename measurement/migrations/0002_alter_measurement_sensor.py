# Generated by Django 4.2.3 on 2023-08-23 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='sensor',
            field=models.IntegerField(),
        ),
    ]
