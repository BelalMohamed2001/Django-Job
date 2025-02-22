from django.contrib import admin 
from django.urls import path 
from . import views

app_name='accounts'
urlpatterns = [
    
    path('signup/', views.sign_up, name='signup'),
    path('profile/',views.profile , name='profile'),
    path('profile/edit',views.editprofile , name='editprofile'),

     

]