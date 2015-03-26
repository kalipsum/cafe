# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0019_basket'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Basket',
        ),
    ]
