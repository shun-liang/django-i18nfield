# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 20:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import i18nfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=190, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', i18nfield.fields.I18nCharField(max_length=190, verbose_name='Book title')),
                ('abstract', i18nfield.fields.I18nTextField(verbose_name='Abstract')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.Author', verbose_name='Author')),
            ],
        ),
    ]