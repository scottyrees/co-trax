# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-06 06:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reco', '0007_auto_20171101_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts_Payable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_date', models.DateField(blank=True)),
                ('vendor', models.CharField(max_length=100)),
                ('bill_value', models.FloatField()),
                ('document', models.FileField(upload_to='documents/')),
                ('bill_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reco.Account_Holder')),
                ('expense_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reco.Expense_Category')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='accounts_payable',
            name='payment_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reco.Payment_Status'),
        ),
    ]
