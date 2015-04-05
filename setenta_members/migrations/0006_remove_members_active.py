# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setenta_members', '0005_auto_20150402_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='active',
        ),
    ]
