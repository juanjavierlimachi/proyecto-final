# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('negocio', '0004_multa_fecha_presentacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='multa',
            name='Usuario',
            field=models.CharField(default='2015-02-02', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='multa',
            name='fecha_presentacion',
            field=models.DateField(),
        ),
    ]
