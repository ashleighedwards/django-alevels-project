# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-09 13:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_auto_20181109_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additem',
            name='user',
        ),
        migrations.RemoveField(
            model_name='addtheitems',
            name='user',
        ),
        migrations.DeleteModel(
            name='AddItem',
        ),
        migrations.DeleteModel(
            name='AddTheItems',
        ),
    ]
