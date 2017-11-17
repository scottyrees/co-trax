# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-13 00:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reco', '0012_auto_20171112_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_Shareholder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lname', models.CharField(max_length=25)),
                ('fname', models.CharField(max_length=25)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reco.Shareholder_Type')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reco.Account_Holder')),
            ],
        ),
    ]
