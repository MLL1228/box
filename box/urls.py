#_author: llm
#_date: 2019-04-01

from django.urls import path
from . import views

app_name = 'box'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('handle_login/', views.handle_login, name='handle_login'),
    path('index/', views.index, name='index'),

]


