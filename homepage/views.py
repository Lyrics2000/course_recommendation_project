from django.shortcuts import render
from accounts.form import (
    SignINForm
)
# Create your views here.
from courses.models import (
    Course,
    CourseCategory,
    AdvertUserLinks
)


def index(request):
    login_form = SignINForm(request.POST,None)


    all_courses = Course.objects.all()
    all_category =  CourseCategory.objects.all()
    adverts = AdvertUserLinks.objects.all()

    context = {
        'courses' : all_courses,
        'course_category': all_category,
        'adverts' : adverts,
        'login':login_form
    }



    return render(request,'index.html',context)



def courses(request):
    all_courses = Course.objects.all()
    all_category =  CourseCategory.objects.all()
    adverts = AdvertUserLinks.objects.all()

    context = {
        'courses' : all_courses,
        'course_category': all_category,
        'adverts' : adverts,
        'len_courses' :  len(all_courses)
    }

    return render(request,'course.html',context)


def raisec(request):
    return render(request,'raisec.html')