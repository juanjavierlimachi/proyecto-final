# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('negocio', '0002_auto_20150610_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='negocio',
            name='categoria',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='negocio',
            name='direccion',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
    ]
