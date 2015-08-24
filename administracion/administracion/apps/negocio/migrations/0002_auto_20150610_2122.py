# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('negocio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multa',
            name='fecha_presentacion',
        ),
        migrations.RemoveField(
            model_name='negocio',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='negocio',
            name='direccion',
        ),
    ]
