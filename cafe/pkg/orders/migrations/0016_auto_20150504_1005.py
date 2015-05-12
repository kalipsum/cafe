# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_basket_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user_hash',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
