# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0013_remove_basket_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('user_hash', models.CharField(max_length=32, unique=True)),
                ('user', models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL, blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='basket',
            old_name='total',
            new_name='price',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=500),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='manager_notes',
            field=models.CharField(blank=True, max_length=1000),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='user_notes',
            field=models.CharField(blank=True, max_length=1000),
            preserve_default=True,
        ),
    ]
