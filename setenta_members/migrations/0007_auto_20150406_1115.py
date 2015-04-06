# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setenta_members', '0006_remove_members_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorizations',
            name='email',
            field=models.EmailField(max_length=100),
            preserve_default=True,
        ),
    ]
