# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('username', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Authorizations',
            fields=[
                ('key', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('expirity', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, serialize=False, primary_key=True)),
                ('city', models.CharField(max_length=50)),
                ('active', models.BooleanField()),
                ('semester', models.IntegerField()),
                ('subjects', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='authorizations',
            name='member',
            field=models.ForeignKey(to='setenta_members.Members'),
            preserve_default=True,
        ),
    ]
