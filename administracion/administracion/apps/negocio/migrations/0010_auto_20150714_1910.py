# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('negocio', '0009_auto_20150714_1909'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categiria',
            new_name='Categoria',
        ),
    ]
