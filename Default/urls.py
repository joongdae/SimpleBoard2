from django.contrib import admin
from django.conf.urls import include
from django.urls import path,include
from . import views
# app_name='Default'
urlpatterns = [
    path('',views.indexshow),
    path('MemJoin/', include('MemJoin.urls'), name='MemJoin'),
    #path('MemJoin/', views.select, name='select'),
    path('LoginClick/', views.LoginClick,name='LoginClick'),
    path('List/',include("BoardList.urls"), name='List')
]
