from django.contrib import admin

# Register your models here.

from .models import (
    Course,
    CourseCategory,
    CourseComments,
    CourseRatings,
    AdvertUserLinks
)


admin.site.register(Course)
admin.site.register(CourseComments)
admin.site.register(CourseCategory)
admin.site.register(CourseRatings)
admin.site.register(AdvertUserLinks)