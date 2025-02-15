from django.shortcuts import render
from .models import Job
def job_list(request):
    job=Job.objects.all()
    
    context ={
        'job':job

    }
    return render(request,'job/joblist.html',context)

def job_detail(request,id):
    jobdetails=Job.objects.get(id=id)
    context ={
        'job':jobdetails

    }
    return render(request,'job/jobdetails.html',context)