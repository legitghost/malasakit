# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-16 05:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcari', '0058_auto_20170911_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='show_statistics',
        ),
    ]