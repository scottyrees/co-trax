# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-13 01:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reco', '0016_auto_20171112_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shares',
            name='personal_shareholder',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='reco.Personal_Shareholder'),
        ),
    ]
