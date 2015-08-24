# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('negocio', '0005_auto_20150619_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='multa',
            name='idUser',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
