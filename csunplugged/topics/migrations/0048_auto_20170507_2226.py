# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-07 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0047_auto_20170507_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glossaryterm',
            name='term',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]