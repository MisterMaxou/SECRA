# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-16 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20161222_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='text',
            field=models.TextField(blank=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='work',
            name='link',
            field=models.CharField(blank=True, default=main.models.generate_link, max_length=30),
        ),
        migrations.AlterField(
            model_name='work',
            name='public',
            field=models.BooleanField(default=True, verbose_name="Visible par d'autres personnes que les contributeurs"),
        ),
    ]
