from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate,login
from .form import (
    SignINForm
)

# Create your views here.


def logout_user(request):
    if request.method=="POST":
        logout(request)
        return redirect("homepage:homepage")
    return redirect("homepage:homepage")


def signIn(request):

    login_form = SignINForm(request.POST,None)

    
    context = {
        'login' : login_form
    }
    if login_form.is_valid:
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password)
        user = authenticate(request,username = username, password = password )
        print("jjja",user)
        if user is not None:
        
            login(request,user)
            return redirect("homepage:homepage")
        else:
            pass
    
    return render(request,'sign-in.html',context)


def signUp(request):
    return render(request,'sign-up.html')