# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetaTag',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=70, null=True)),
                ('property', models.CharField(max_length=70, null=True)),
                ('content', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('relative_url', models.CharField(max_length=100, unique=True)),
                ('title', models.CharField(max_length=70)),
                ('template', models.CharField(max_length=50, default='page-default.html')),
                ('content', models.TextField()),
                ('access_count', models.BigIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='metatag',
            name='page',
            field=models.ForeignKey(related_name='meta_tags', to='pages.Page'),
        ),
    ]
