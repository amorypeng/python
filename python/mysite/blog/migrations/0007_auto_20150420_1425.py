# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150420_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=redactor.fields.RedactorField(verbose_name='Text'),
        ),
    ]
