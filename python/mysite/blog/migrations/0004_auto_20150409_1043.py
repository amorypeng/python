# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150409_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(default='yolo', max_length=100),
        ),
    ]
