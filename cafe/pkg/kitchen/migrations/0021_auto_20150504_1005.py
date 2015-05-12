# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0020_delete_basket'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='cnt_in_store',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='weight_in_store',
            field=models.IntegerField(default=500),
            preserve_default=False,
        ),
    ]
