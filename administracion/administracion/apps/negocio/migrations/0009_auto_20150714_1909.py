# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('negocio', '0008_remove_negocio_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categiria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoria', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='negocio',
            name='tipo',
        ),
        migrations.AddField(
            model_name='negocio',
            name='categoria',
            field=models.ForeignKey(default=2, to='negocio.Categiria'),
            preserve_default=False,
        ),
    ]
