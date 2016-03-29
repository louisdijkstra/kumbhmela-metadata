# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0014_drive_external'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drive',
            name='time_added',
            field=models.DateTimeField(blank=True, help_text='Time when the drive was added to the drive bay.', null=True),
        ),
        migrations.AlterField(
            model_name='drive',
            name='time_removed',
            field=models.DateTimeField(blank=True, help_text='Time when the drive was removed from the drive bay.', null=True),
        ),
    ]
