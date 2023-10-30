from django.contrib import admin
from django.urls import path,include
from . import views

app_name='WriteBoard'
urlpatterns = [
    path('', views.writeboard1, name="SelectBoard"),
    #path('writeboard/', include('WriteBoard.urls'), name="WriteBoard"),
    path('Board_Insert/', views.Board_Insert, name="Board_Insert"),
]
