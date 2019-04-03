from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login  # 使用django内置的authenticate进行验证
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.


def login_auth(func):
    def inner(request):
        is_login = request.session.get('is_login', False)
        if not is_login:
            return redirect('/box/login')
        else:
            return func(request)
    return inner


def login(request):
    return render(request, 'login.html')


def handle_login(request):
    if request.method != 'POST':
        return redirect('/box/login/')
    else:
        username = request.POST['username']
        password = request.POST['password']

        # # ldap验证: 因为前面已经配置过ldap， 所以这里会去和ldap的帐户进行验证
        # user = authenticate(username=username, password=password)

        # 解析 ldap cookie， 如果没有通过返回 login 界面

        # 通过验证，查询此账号是否在 box_user 中，不在的话 1。 添加新账号，并设定权限、创建时间和上次登陆时间 2。 设置cookie和session，并设置过期时间 3。 跳转到 index 页面

        request.session['is_login'] = True
        request.session['username'] = username

        return redirect('/box/index/')


def logout(request):
    # 如果有有效的 cookie 和 session，cookie 和 session 设置为过期
    try:
        # 将 session 置为失效
        del request.session['is_login']

        # ORM -----------> request.session.flush()  删除 django-session 表中的对应一行记录

    except KeyError:
        pass


    return redirect('/box/login/')


@login_auth
def index(request):
    if request.method == 'GET':
        cookie_content = request.COOKIES
        session_content = request.session

        print(cookie_content, session_content)

        return render(request, 'index.html')





