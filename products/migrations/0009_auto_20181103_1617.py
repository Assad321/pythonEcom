# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-03 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20181010_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('1', 'Fruit'), ('2', 'Vegetable'), ('3', 'Other')], default=1, max_length=10),
        ),
    ]
