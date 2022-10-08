from django.contrib import admin

# Register your models here.

from .models import (
    Course,
    CourseCategory,
  
    AdvertUserLinks,CourseRattingAndComment
)


admin.site.register(Course)

admin.site.register(CourseCategory)

admin.site.register(AdvertUserLinks)
admin.site.register(CourseRattingAndComment)