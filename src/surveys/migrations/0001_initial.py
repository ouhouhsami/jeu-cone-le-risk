# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-19 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('innodation', models.BooleanField()),
                ('argile', models.BooleanField()),
                ('mouvement_terrain', models.BooleanField()),
                ('cavite', models.BooleanField()),
                ('seisme', models.BooleanField()),
                ('sites_pollues', models.BooleanField()),
                ('installations_classees', models.BooleanField()),
                ('canalisation', models.BooleanField()),
                ('nucleair', models.BooleanField()),
            ],
        ),
    ]
