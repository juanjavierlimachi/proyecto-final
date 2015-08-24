# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('negocio', '0007_negocio_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='negocio',
            name='categoria',
        ),
    ]
