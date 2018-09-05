# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-03 02:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appconf', '0003_auto_20180823_1604'),
        ('broken_record', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brokenrrecord',
            name='project',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='appconf.Project', verbose_name='所属项目'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='brokenrrecord',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appconf.Product', verbose_name='所属产品线'),
        ),
    ]