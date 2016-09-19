# coding:utf-8
from django import forms
# from todolist.models import Todo


#一，  用django forms定义表单
class TodoForm(forms.Form):
    content = forms.CharField(label='事件', error_messages={'required': '事件内容不能为空'})


class EditForm(forms.Form):
    content = forms.CharField(label='事件', error_messages={'required': '事件内容不能为空'})

#二， 用django modelform定义表单
# class TodoForm(forms.ModelForm):
#     class Meta:
#         model = Todo
#         fields = ('content',)  #定义需要显示的字段
        # exclude = ('time', 'status', 'edit_status', 'id') #定义不需要显示的字段


