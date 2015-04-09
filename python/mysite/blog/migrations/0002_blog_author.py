# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.TextField(default=datetime.datetime(2015, 4, 9, 17, 39, 5, 105572, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
