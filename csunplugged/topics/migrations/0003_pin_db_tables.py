# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 00:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0002_topic_slug'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='topic',
            table='topics_topic',
        ),
    ]
