# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='multa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hora', models.CharField(max_length=12)),
                ('fecha_notificacion', models.DateTimeField(auto_now=True)),
                ('descripcion', models.TextField()),
                ('Codigo', models.IntegerField()),
                ('fecha_presentacion', models.DateField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Negocio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('propietario', models.CharField(max_length=100)),
                ('memorial_apertura', models.CharField(max_length=20)),
                ('resolucion_municipal', models.CharField(max_length=20)),
                ('categoria', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
