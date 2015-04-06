# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setenta_members', '0007_auto_20150406_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorizations',
            name='email',
            field=models.EmailField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
