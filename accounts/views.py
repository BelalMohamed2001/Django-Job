from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import ProfileForm, SignupForm, UserForm
from .models import Profile
# Create your views here.
def sign_up(request):
    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            #to make authintication and close session of admin and genrate new session of user
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(username=username,password=password) #if user and pass min database or not
            login(request,user)
            return redirect('/accounts/profile')

    else:
        form=SignupForm()
    return render(request,'registration/signup.html',{'form':form})


def profile(request):
     profile = Profile.objects.get(user=request.user)
     return render(request,'accounts/profile.html',{'profile': profile})

def editprofile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method=="POST":
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profile)
        if userform.is_valid and profileform.is_valid:
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))



    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    return render(request,'accounts/profile_edit.html',{'userform':userform,'profileform':profileform})