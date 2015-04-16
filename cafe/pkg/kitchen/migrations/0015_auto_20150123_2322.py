# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0014_auto_20150123_2236'),
    ]

    operations = [
        migrations.CreateModel(
            name='DishComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('weight', models.FloatField()),
                ('dish_ID', models.ForeignKey(to='kitchen.Dish')),
                ('ingredient_ID', models.ForeignKey(to='kitchen.Ingredient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='dishcomponents',
            name='dish_ID',
        ),
        migrations.RemoveField(
            model_name='dishcomponents',
            name='ingredient_ID',
        ),
        migrations.DeleteModel(
            name='DishComponents',
        ),
    ]
