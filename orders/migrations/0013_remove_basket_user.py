# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_order_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='user',
        ),
    ]
