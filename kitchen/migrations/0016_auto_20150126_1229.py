# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0015_auto_20150123_2322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='category_ID',
            new_name='category_id',
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='menu_ID',
            new_name='menu_id',
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='dish_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='dishcomponent',
            old_name='dish_ID',
            new_name='dish_id',
        ),
        migrations.RenameField(
            model_name='dishcomponent',
            old_name='ingredient_ID',
            new_name='ingredient_id',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='ing_name',
            new_name='name',
        ),
    ]
