# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-17 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180317_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='', upload_to='image/%Y/%m', verbose_name='\u5934\u50cf'),
        ),
    ]