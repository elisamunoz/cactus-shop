# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-23 22:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='label',
        ),
    ]
