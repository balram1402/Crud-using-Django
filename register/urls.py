from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.registerform,name='registerform'),
    path('userslist/',views.userslist,name='userslist'),
    path('delete/<int:id>',views.delete,name='delete'),
]