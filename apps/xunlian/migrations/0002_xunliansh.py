# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-04-25 17:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yundongyuan', '0001_initial'),
        ('xunlian', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='XunlianSh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('riqi', models.DateField(blank=True, default='2010-01-01', null=True, verbose_name='训练日期')),
                ('gaotong', models.FloatField(verbose_name='睾酮')),
                ('xingming', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yundongyuan.Athlete', verbose_name='队员姓名')),
            ],
            options={
                'verbose_name_plural': '训练-生化',
                'verbose_name': '训练-生化',
            },
        ),
    ]