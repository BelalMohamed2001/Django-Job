from django.contrib import admin 
from django.urls import path ,include
from . import views

app_name='job'
urlpatterns = [
    
    path('',views.job_list , name='job_list'),
    path('addjob',views.add_job , name='addjob'),
    
    path('<str:slug>',views.job_detail , name='job_detail'),

]