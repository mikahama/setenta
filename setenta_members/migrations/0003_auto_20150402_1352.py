# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setenta_members', '0002_auto_20150402_0815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authorizations',
            name='member',
        ),
        migrations.AddField(
            model_name='authorizations',
            name='email',
            field=models.EmailField(default='', max_length=100, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='authorizations',
            name='key',
            field=models.CharField(max_length=100, primary_key=True),
            preserve_default=True,
        ),
    ]
