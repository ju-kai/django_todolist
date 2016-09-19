# coding:utf-8
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from todolist.forms import TodoForm, EditForm
from todolist.models import Todo
# Create your views here.


#主页及分页功能
def index(request):

    todo_form = TodoForm()
    posts = Todo.objects.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'demo.html', locals())


#添加事件
def add(request):

    #二，forms中使用Form时
    if request.method == 'POST':
        # 初始化表单，将用户的值提交到表单
        todo_form = TodoForm(request.POST)
        if todo_form.is_valid():
            Todo.objects.create(
                content=todo_form.cleaned_data['content'],
            )
            return redirect('/index')
            # return HttpResponse('add succeed')
    else:
        todo_form = TodoForm()
    posts = Todo.objects.all()
    return render(request, 'demo.html', locals())
#
#
#     # 一，自定义表单提交
#     # if request.method == 'POST':
#     # content = request.POST['content']
#     # Todo.objects.create(
#     #     content=content,
#     # )
#     # return HttpResponse('add succeed!!!')
#     # else:
#     # return render(request, 'index.html', locals())
#
#     #三， forms使用ModelForm时
#     # if request.method == 'POST':
#     #     todo_form = TodoForm(request.POST)
#     #     if todo_form.is_valid():
#     #         todo_form.save()
#     #         return HttpResponse('添加事件成功')
#     # else:
#     #     todo_form = TodoForm()
#     # posts = Todo.objects.all()
#     # for post in posts:
#     #     print(post.content)
#     #     print(post.time)
#     # return render(request, 'index.html', locals())


#删除事件
def delete(request, id):

    if request.method == 'GET':
        Todo.objects.filter(id=id).delete()
        return redirect('/index')
    posts = Todo.objects.all()
    return render(request, 'demo.html', locals())


#正在编辑
def editing(request, id):

    if request.method == 'GET':
        Todo.objects.filter(id=id).update(edit_status=1)
        return redirect('/index')
    posts = Todo.objects.all()
    return render(request, 'demo.html', locals())


# #编辑完成
def edited(request, id):
    if request.method == 'POST':
        todo_form = TodoForm()
        edit_form = EditForm(request.POST)
        if edit_form.is_valid():
            content = edit_form.cleaned_data['content']
            print(content)
            Todo.objects.filter(id=id).update(content=content, edit_status=0)
            return redirect('/index')
        else:
            todo_form = TodoForm()
            edit_form = EditForm()
    posts = Todo.objects.all()
    return render(request, 'demo.html', locals())


# 事件状态改为完成
def done(request, id):

    if request.method == 'GET':
        Todo.objects.filter(id=id).update(status=1)
        return redirect('/index')
    posts = Todo.objects.all()
    return render(request, 'demo.html', locals())


# 事件状态改为未完成
def undone(request, id):

    if request.method == 'GET':
        Todo.objects.filter(id=id).update(status=0)
        return redirect('/index')
    posts = Todo.objects.all()
    return render(request, 'demo.html', locals())

