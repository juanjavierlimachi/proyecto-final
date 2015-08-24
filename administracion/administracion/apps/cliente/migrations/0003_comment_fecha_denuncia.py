# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_remove_comment_fecha_denuncia'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='fecha_denuncia',
            field=models.DateTimeField(default='2015-02-02', auto_now=True),
            preserve_default=False,
        ),
    ]
