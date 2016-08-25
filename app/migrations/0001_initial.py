# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('shortname', models.CharField(max_length=200)),
                ('startdate', models.DateField()),
                ('addeddate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-addeddate'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=600)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
    ]