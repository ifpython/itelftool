# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-03 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broken_record', '0008_auto_20180903_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='brokenrrecord',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='brokenrrecord',
            name='broken_department',
            field=models.CharField(choices=[('运维部', '运维部'), ('星星打车技术部', '星星打车技术部'), ('其他', '其他')], max_length=30, verbose_name='故障主要归属部门'),
        ),
        migrations.AlterField(
            model_name='brokenrrecord',
            name='broken_status_type',
            field=models.CharField(choices=[('已解决', '已解决'), ('处理中', '处理中'), ('搁置中', '搁置中')], max_length=30, verbose_name='故障状态类型'),
        ),
        migrations.AlterField(
            model_name='brokenrrecord',
            name='broken_type',
            field=models.CharField(choices=[('网络', '网络'), ('CDN缓存', 'CDN缓存'), ('数据库', '数据库'), ('Web容器', 'Web容器'), ('安全漏洞', '安全漏洞'), ('中间件', '中间件'), ('操作系统', '操作系统'), ('域名', '域名'), ('硬件', '硬件'), ('其他', '其他')], max_length=30, verbose_name='故障类型'),
        ),
        migrations.AlterField(
            model_name='brokenrrecord',
            name='severity_type',
            field=models.CharField(choices=[('非常高', '非常高'), ('高', '高'), ('中', '中'), ('低', '低')], max_length=30, verbose_name='故障严重性'),
        ),
    ]
