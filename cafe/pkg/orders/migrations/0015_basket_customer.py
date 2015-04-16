# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20150325_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='customer',
            field=models.ForeignKey(default=1, to='orders.Customer'),
            preserve_default=False,
        ),
    ]
