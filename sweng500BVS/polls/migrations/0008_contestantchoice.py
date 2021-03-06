# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 20:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20170331_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContestantChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contestant_name', models.CharField(max_length=200)),
                ('contestant_address', models.CharField(choices=[('mpMtRQUB9XeyXiJevZL6TuLxbvNJJys74j', 'Voter1Address'), ('miyLyx2bp4buCnRV4y93RKNH3Lp1s89zQa', 'voter2Address'), ('n39HtcDLnXrxNH4yEra8K7QfVKLN2CJ3Sk', 'voter3Address')], max_length=36)),
                ('ballot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Ballot')),
            ],
        ),
    ]
