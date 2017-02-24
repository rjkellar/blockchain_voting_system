# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 15:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ballot',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='end date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_address',
            field=models.CharField(default='ENTER BLOCKCHAIN ADDRESS HERE', max_length=36),
            preserve_default=False,
        ),
    ]
