# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('negocio', '0003_auto_20150610_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='multa',
            name='fecha_presentacion',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
