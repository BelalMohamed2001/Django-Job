from django.contrib import admin 
from django.urls import path ,include
from . import views ,api


app_name='job'
urlpatterns = [
    
    path('',views.job_list , name='job_list'),
    path('addjob',views.add_job , name='addjob'),
    
    path('<str:slug>',views.job_detail , name='job_detail'),
    

    ## api
    path('api/jobs',api.joblist , name='job_list_api'),
    path('api/jobs/<int:id>',api.job_details, name='job_detail_api'),


    ## class based views
    path('api/v2/jobs',api.JobListApi.as_view() , name='job_list_api'),
    path('api/v2/jobs/<int:id>',api.JobDetail.as_view() , name='job_detail_api'),



]