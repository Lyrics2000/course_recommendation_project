from email.policy import default
from django.db import models
from accounts.models import UserTable
import os
import random


# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance,filename):
    new_filename = random.randint(1,999992345677653234)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext = ext)
    return "courses/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename = final_filename )


class CourseCategory(models.Model):
    category_name = models.CharField(max_length  = 255)


    def __str__(self) -> str:
        return self.category_name



class Course(models.Model):
    user = models.ForeignKey(UserTable,on_delete = models.CASCADE , blank  = True , null = True)
    category_name = models.ForeignKey(CourseCategory,on_delete = models.CASCADE)
    university = models.CharField(max_length =  255)
    course_title = models.CharField(max_length =  255)
    course_image = models.ImageField(upload_to =  upload_image_path)
    short_description = models.CharField(max_length = 255 , blank = True,null = True)
    course_description =  models.TextField()
    ratting_percentage = models.PositiveBigIntegerField(blank = True,null = True)
    is_published = models.BooleanField(default = True)


    def __str__(self) -> str:
        return self.course_title





class CourseRatings(models.Model):
     user = models.ForeignKey(UserTable,on_delete = models.CASCADE , blank  = True , null = True)
     course = models.ForeignKey(Course,on_delete = models.CASCADE)
     rattings = models.PositiveBigIntegerField()


     def __str__(self) -> str:
         return str(self.course)



class CourseComments(models.Model):
     user = models.ForeignKey(UserTable,on_delete = models.CASCADE , blank  = True , null = True)
     course = models.ForeignKey(Course,on_delete = models.CASCADE)
     comment = models.CharField(max_length =  255)


     def __str__(self) -> str:
         return str(self.course)




class AdvertUserLinks(models.Model):
    user_image = models.ImageField(upload_to =  upload_image_path)
    ig_link = models.URLField()

    def __str__(self) -> str:
        return self.ig_link



    


