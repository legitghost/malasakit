# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-01 22:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feature_phone', '0011_auto_20180129_0122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='respondent',
            options={'default_permissions': ('add', 'change', 'delete', 'view')},
        ),
    ]
