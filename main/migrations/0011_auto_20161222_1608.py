# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-22 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20161217_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='link',
            field=models.CharField(default=main.models.generate_link, max_length=30),
        ),
    ]
