# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-18 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0030_appconfig_protocolo_manual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appconfig',
            name='protocolo_manual',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=False, verbose_name='Informar data e hora de protocolo?'),
        ),
    ]
