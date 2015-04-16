# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0016_auto_20150126_1229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='menu_id',
            new_name='menu',
        ),
        migrations.RenameField(
            model_name='dishcomponent',
            old_name='dish_id',
            new_name='dish',
        ),
        migrations.RenameField(
            model_name='dishcomponent',
            old_name='ingredient_id',
            new_name='ingredient',
        ),
    ]
