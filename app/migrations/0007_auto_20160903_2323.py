# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 23:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20160903_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='shortname',
            new_name='person',
        ),
    ]