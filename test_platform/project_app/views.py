from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from project_app.models import Project
from project_app.form import projectForm
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

@login_required #判断用户是否登录
def project_manage(request):
    # username = request.COOKIES.get('user','')
    username = request.session.get('user', '')
    project_all = Project.objects.all()
    print()
    return render(request, "project_manage.html",{
        "user":username,
        "projects":project_all,
        "type":"list"
        })

@login_required
def add_project(request):
    """
    添加项目
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = projectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            Project.objects.create(name=name,describe=describe)
            return HttpResponseRedirect('/manage/project_manage/')
    else:
        form = projectForm()
    return render(request, "project_manage.html",{
        "type":"add",
        'form':form
    })

@login_required
def edit_project(request,pid):
    if request.method == 'POST':
        form = projectForm(request.POST)
        if form.is_valid():
            model = Project.objects.get(id=pid)
            model.name = form.cleaned_data['name']
            model.describe = form.cleaned_data['describe']
            model.save()
            return HttpResponseRedirect('/manage/project_manage/')
    else:
        if pid:
            form = projectForm(
                instance=Project.objects.get(id=pid))
    return render(request, "project_manage.html",{
        "type":"edit",
        'form':form
    })