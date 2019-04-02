from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login  # 使用django内置的authenticate进行验证
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.


def login(request):
    return render(request, 'login.html')


def handle_login(request):
    if request.method == 'GET':
        return redirect('/box/login/')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # # ldap验证: 因为前面已经配置过ldap， 所以这里会去和ldap的帐户进行验证
        # user = authenticate(username=username, password=password)
        # # 验证完成后，使用Django 的登录函数进行登录
        # auth_login(request, user)

        print(username, password)
        return redirect('/box/index/')


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


