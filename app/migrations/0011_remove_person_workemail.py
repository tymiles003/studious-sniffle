# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-04 16:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20160904_0346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='workemail',
        ),
    ]