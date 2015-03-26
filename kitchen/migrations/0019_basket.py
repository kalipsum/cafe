# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0018_menu_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
