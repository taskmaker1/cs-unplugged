# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 01:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0004_rename_tables'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
