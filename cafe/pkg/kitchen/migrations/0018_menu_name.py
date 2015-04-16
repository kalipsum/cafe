# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0017_auto_20150127_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 1, 30, 9, 20, 56, 22276, tzinfo=utc), max_length=70),
            preserve_default=False,
        ),
    ]
