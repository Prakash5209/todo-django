from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def userlogin(request):
    form=AuthenticationForm(request.POST or None)
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('task:TaskClassView')
    context={'form':form}
    return render(request,'login.html',context)

def userlogout(request):
    logout(request)
    return redirect('task:TaskClassView')
    