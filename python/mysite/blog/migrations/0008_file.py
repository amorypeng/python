# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150420_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('upload', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('is_image', models.BooleanField(default=True)),
            ],
        ),
    ]
