# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-29 01:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reco', '0002_auto_20171023_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='account_holder',
            name='entry_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
