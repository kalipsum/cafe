# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20150314_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='order',
            field=models.ForeignKey(blank=True, to='orders.Order'),
            preserve_default=True,
        ),
    ]
