# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_remove_projects_dashboard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dashboard_view',
            field=models.IntegerField(choices=[(1, 'Your subscriptions'), (2, 'Your languages'), (4, 'Component list')], default=1, verbose_name='Default dashboard view'),
        ),
    ]
