# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-12 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0012_auto_20190912_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='alerted_over_plan_limit',
            field=models.BooleanField(default=False),
        ),
    ]
