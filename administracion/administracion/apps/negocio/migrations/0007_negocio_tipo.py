# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('negocio', '0006_multa_iduser'),
    ]

    operations = [
        migrations.AddField(
            model_name='negocio',
            name='tipo',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
