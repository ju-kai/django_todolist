# coding:utf-8
from django.db import models
from datetime import datetime


# Create your models here.


class Todo(models.Model):
    content = models.TextField(max_length=30, verbose_name='内容')
    time = models.TimeField(default=datetime.now, verbose_name='发布时间')
    status = models.IntegerField(default=0, verbose_name='完成状态')
    edit_status = models.IntegerField(default=0, verbose_name='编辑状态')

    class Meta:
        verbose_name = '事件内容'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.content
