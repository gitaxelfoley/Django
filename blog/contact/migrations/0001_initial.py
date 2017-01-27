# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 19:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('text', models.TextField()),
                ('email', models.CharField(max_length=120)),
            ],
        ),
    ]