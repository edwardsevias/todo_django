# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-27 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=128)),
                ('is_done', models.BooleanField(default=False)),
            ],
        ),
    ]
