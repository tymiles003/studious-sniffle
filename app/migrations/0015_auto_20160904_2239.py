# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 02:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20160904_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='personalcity',
            field=models.CharField(default='Hartford', max_length=50, verbose_name='Home city'),
        ),
        migrations.AddField(
            model_name='person',
            name='personalstate',
            field=models.CharField(default='CT', max_length=50, verbose_name='Home state'),
        ),
        migrations.AddField(
            model_name='person',
            name='personalstreet',
            field=models.CharField(blank=True, max_length=50, verbose_name='Home street address'),
        ),
        migrations.AddField(
            model_name='person',
            name='personalzip',
            field=models.CharField(blank=True, max_length=5, verbose_name='Home zip code'),
        ),
        migrations.AddField(
            model_name='person',
            name='workcity',
            field=models.CharField(default='Hartford', max_length=50, verbose_name='Work city'),
        ),
        migrations.AddField(
            model_name='person',
            name='workstate',
            field=models.CharField(default='CT', max_length=50, verbose_name='Work state'),
        ),
        migrations.AddField(
            model_name='person',
            name='workstreet',
            field=models.CharField(blank=True, max_length=50, verbose_name='Work street address'),
        ),
        migrations.AddField(
            model_name='person',
            name='workzip',
            field=models.CharField(blank=True, max_length=5, verbose_name='Work zip code'),
        ),
    ]
