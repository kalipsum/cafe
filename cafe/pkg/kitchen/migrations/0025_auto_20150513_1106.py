# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0024_auto_20150513_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='count',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
