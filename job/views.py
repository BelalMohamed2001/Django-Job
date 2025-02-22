from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from job.filters import ProductFilter
from job.form import ApplyForm ,AddJob
from .models import Job
def job_list(request):
    job=Job.objects.all()
    ## filters
    filter = ProductFilter(request.GET, queryset=job)
    job=filter.qs
    paginator = Paginator(job, 2) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context ={
        'job':page_obj,
        'filter':filter

    }
    return render(request,'job/joblist.html',context)

def job_detail(request,slug):
    jobdetails=Job.objects.get(slug=slug)
    if request.method=="POST":
        form=ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = jobdetails
            myform.save()
           
    else:
        
        form = ApplyForm()
    context ={
        'job':jobdetails,'form':form

    }
    return render(request,'job/jobdetails.html',context)

@login_required
def add_job(request):
  
    if request.method=="POST":
        form=AddJob(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner=request.user#save the person make login in my form  nd admin has id 1 for fist migrations
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form=AddJob()
        return render(request,'job/addjob.html',{'form':form})