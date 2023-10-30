from django.contrib import admin
from django.urls import path,include
from . import views

app_name='MemJoin'
urlpatterns = [
    path('', views.select , name='select'),
    path('Mem_Insert/', views.Mem_Insert, name="Mem_Insert"),
    path('Confirm1/', views.Confirm1, name="Confirm1"),
]
