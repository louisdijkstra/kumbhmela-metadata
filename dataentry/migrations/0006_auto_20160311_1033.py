# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-11 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0005_auto_20160311_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='end_recording',
            field=models.DateTimeField(blank=True, help_text='Time when the recording ended (optional).', null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='start_recording',
            field=models.DateTimeField(blank=True, help_text='Time when the recording started (optional).', null=True),
        ),
    ]
