from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request,'index.html')



def courses(request):
    return render(request,'course.html')


def raisec(request):
    return render(request,'raisec.html')