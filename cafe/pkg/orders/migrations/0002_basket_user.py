# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='user',
            field=models.CharField(blank=True, max_length=70),
            preserve_default=True,
        ),
    ]
