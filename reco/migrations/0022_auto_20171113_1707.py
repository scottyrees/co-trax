# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-14 01:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reco', '0021_auto_20171113_1540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personal_shareholder',
            old_name='lname',
            new_name='name',
        ),
    ]
