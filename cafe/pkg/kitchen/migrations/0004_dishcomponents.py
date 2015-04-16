# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0003_ingredient'),
    ]

    operations = [
        migrations.CreateModel(
            name='DishComponents',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('dish_ID', models.ForeignKey(to='kitchen.Dish')),
                ('ingredient_ID', models.ForeignKey(to='kitchen.Ingredient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
