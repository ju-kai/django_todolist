# coding:utf-8
from django.contrib import admin
from todolist.models import *
# Register your models here.

#将models中的数据库模型注册到admin
admin.site.register(Todo)