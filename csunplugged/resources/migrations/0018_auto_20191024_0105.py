# Generated by Django 2.2.3 on 2019-10-24 01:05

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0017_auto_20190208_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=list, size=None),
        ),
    ]