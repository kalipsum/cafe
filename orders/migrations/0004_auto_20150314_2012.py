# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20150314_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitems',
            name='dish',
        ),
        migrations.RemoveField(
            model_name='orderitems',
            name='order',
        ),
        migrations.DeleteModel(
            name='OrderItems',
        ),
        migrations.AddField(
            model_name='basket',
            name='order',
            field=models.ForeignKey(default=1, to='orders.Order'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
