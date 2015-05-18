# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0021_auto_20150504_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='count',
            field=models.IntegerField(default=3, editable=False),
            preserve_default=False,
        ),
    ]
