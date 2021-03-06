# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-21 09:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import redactor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas', '0006_persona_fotos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acerca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('informacion', redactor.fields.RedactorField(verbose_name='Informacion')),
                ('actualizacion', models.DateTimeField(default=datetime.datetime(2017, 4, 21, 9, 15, 45, 108574, tzinfo=utc), verbose_name='Ultima actualizacion')),
            ],
            options={
                'verbose_name': 'Acerca',
                'verbose_name_plural': 'Acerca',
            },
        ),
        migrations.CreateModel(
            name='Integrante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('idPersonaRef', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='personas.Persona', verbose_name='Persona')),
            ],
        ),
        migrations.CreateModel(
            name='Tercero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('url', models.URLField(verbose_name='Direccion web')),
                ('logo', models.ImageField(upload_to='logos/terceros/', verbose_name='Logo')),
            ],
        ),
        migrations.CreateModel(
            name='TipoIntegrante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
            ],
        ),
        migrations.AddField(
            model_name='integrante',
            name='idTipoIntegranteRef',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.TipoIntegrante', verbose_name='Tipo integrante'),
        ),
    ]
