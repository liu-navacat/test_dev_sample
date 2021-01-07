from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
# 主要代码逻辑放在这里

def index(request):
    return render(request,"index.html")

#处理登录请求#

def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username","")
        password = request.POST.get("password","")

        if username == "" or password == "":
            return render(request, "index.html",
                          {"error":"用户名或密码为空"})
        else:
            user = auth.authenticate(username = username,password = password)
            if user is not None:
                auth.login(request,user) #记录用户的登录状态
                # response =  HttpResponseRedirect("/project_manage/")
                # response.set_cookie('user',username,3600)
                # return response
                request.session['user'] = username
                return HttpResponseRedirect('/manage/project_manage/')
            else:
                return render(request, "index.html",
                          {"error": "用户名或密码错误"})


# 退出登录
def logout(request):
    auth.logout(request) #清除用户的登录状态
    response = HttpResponseRedirect('/')
    return response



