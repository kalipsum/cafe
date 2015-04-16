# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=70)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('total', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
