from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def registration(request):
    ufo=UserForm()
    pfo=profileForm()
    d={'ufo':ufo,'pfo':pfo}

    
    if request.method=='POST' and request.FILES:
        UFD=UserForm(request.POST)
        PFD=profileForm(request.POST,request.FILES)
        if UFD.is_valid() and PFD.is_valid():
            MUFDO=UFD.save(commit=False)
            pw=UFD.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()

            MPFDO=PFD.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            return HttpResponse('register successfully')
        else:
            return HttpResponse('invalid')



    return render(request,'registration.html',d)

