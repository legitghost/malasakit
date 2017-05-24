# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-25 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcari', '0020_comment_tagalog_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='num_rated',
            new_name='number_rated',
        ),
        migrations.AddField(
            model_name='comment',
            name='average_score',
            field=models.IntegerField(default=0),
        ),
    ]