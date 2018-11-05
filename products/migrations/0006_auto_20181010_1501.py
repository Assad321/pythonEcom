# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-10 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[(1, 'GREEN'), (2, 'BLUE'), (3, 'RED'), (4, 'ORANGE'), (5, 'BLACK')], default=1, max_length=6),
        ),
    ]