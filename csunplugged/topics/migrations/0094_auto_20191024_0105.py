# Generated by Django 2.2.3 on 2019-10-24 01:05

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0093_auto_20190208_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agegroup',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='classroomresource',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='curriculumarea',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='curriculumintegration',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='glossaryterm',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='learningoutcome',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='programmingchallenge',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='programmingchallengedifficulty',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='programmingchallengeimplementation',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='programmingchallengelanguage',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='resourcedescription',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='topic',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='unitplan',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=list, size=None),
        ),
    ]