# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setenta_members', '0004_auto_20150402_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorizations',
            name='email',
            field=models.EmailField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='authorizations',
            name='key',
            field=models.CharField(max_length=200, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
