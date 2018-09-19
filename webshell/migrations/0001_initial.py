# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-14 03:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appconf', '0003_auto_20180823_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='webshell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddr', models.GenericIPAddressField(unique=True, verbose_name='服务器IP')),
                ('username', models.CharField(max_length=50, verbose_name='用户名')),
                ('password', models.CharField(max_length=50, verbose_name='密码')),
                ('port', models.IntegerField(blank=True, default=22, null=True, verbose_name='SSH端口')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appconf.Product', verbose_name='所属产品线')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appconf.Project', verbose_name='所属项目')),
            ],
        ),
    ]