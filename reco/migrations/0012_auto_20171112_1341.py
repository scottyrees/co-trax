# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-12 21:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reco', '0011_auto_20171112_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shareholder_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='shareholder',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='reco.Shareholder_Type'),
        ),
    ]
