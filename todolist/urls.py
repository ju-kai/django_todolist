# coding:utf-8

from django.conf.urls import url
from todolist import views


urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^delete/(.+)', views.delete, name='delete'),
    url(r'^editing/(.+)', views.editing, name='editing'),
    url(r'^edited/(.+)', views.edited, name='edited'),
    url(r'^done/(.+)', views.done, name='done'),
    url(r'^undone/(.+)', views.undone, name='undone'),
]
