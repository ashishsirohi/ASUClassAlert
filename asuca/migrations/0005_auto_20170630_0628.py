# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 06:28
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asuca', '0004_auto_20170626_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='users',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None),
        ),
    ]