# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userpro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=380)),
                ('description', models.CharField(max_length=3000000)),
                ('views', models.IntegerField(default=0)),
                ('picture', models.ImageField(upload_to=b'project_image', blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('category', models.ForeignKey(to='projects.Category')),
                ('companyprofile', models.ForeignKey(default=1, to='userpro.CompanyProfile')),
            ],
        ),
    ]
