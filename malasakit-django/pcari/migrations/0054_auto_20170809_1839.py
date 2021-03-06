# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcari', '0053_auto_20170804_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optionquestion',
            name='_options_text',
            field=models.TextField(blank=True, default=b'[]', verbose_name='Options as JSON list'),
        ),
        migrations.AlterField(
            model_name='quantitativequestion',
            name='max_score',
            field=models.PositiveSmallIntegerField(default=9, null=True, verbose_name='Minimum score'),
        ),
        migrations.AlterField(
            model_name='quantitativequestion',
            name='min_score',
            field=models.PositiveSmallIntegerField(default=0, null=True, verbose_name='Maximum score'),
        ),
    ]
