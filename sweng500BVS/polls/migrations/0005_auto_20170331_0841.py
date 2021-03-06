# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20170325_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='ballot',
            name='ballot_issued',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ballot',
            name='ballot_address',
            field=models.CharField(choices=[('ballot1', 'mh4w5JnU662ddHywJU3X1wYL6mufjd6Egz')], max_length=36),
        ),
        migrations.AlterField(
            model_name='choice',
            name='voter_address',
            field=models.CharField(choices=[('voter1', 'mpMtRQUB9XeyXiJevZL6TuLxbvNJJys74j'), ('voter2', 'miyLyx2bp4buCnRV4y93RKNH3Lp1s89zQa'), ('voter3', 'n39HtcDLnXrxNH4yEra8K7QfVKLN2CJ3Sk')], max_length=36),
        ),
    ]
