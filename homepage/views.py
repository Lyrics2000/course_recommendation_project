from django.shortcuts import render
import pandas as pd
from scipy.sparse import csr_matrix
import numpy as np
from accounts.form import (
    SignINForm
)
# Create your views here.
from courses.models import (
    Course,
    CourseCategory,
    AdvertUserLinks,
    CourseRattingAndComment
)
from sklearn.neighbors import NearestNeighbors
from django.contrib.auth.decorators import login_required



def create_matrix(df):
	
	N = len(df['user'].unique())
	M = len(df['course'].unique())
	
	# Map Ids to indices
	user_mapper = dict(zip(np.unique(df["user"]), list(range(N))))
	course_mapper = dict(zip(np.unique(df["course"]), list(range(M))))
 
   
	
	# Map indices to IDs
	user_inv_mapper = dict(zip(list(range(N)), np.unique(df["user"])))
	course_inv_mapper = dict(zip(list(range(M)), np.unique(df["course"])))
	
	user_index = [user_mapper[i] for i in df['user']]
	movie_index = [course_mapper[i] for i in df['course']]

	X = csr_matrix((df["ratings"], (movie_index, user_index)), shape=(M, N))
	
	return X, user_mapper, course_mapper, user_inv_mapper, course_inv_mapper


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




def courseDetails(request,id):

    one_course =  Course.objects.get(id = id)
    all_category =  CourseCategory.objects.all()
    course_rattings = CourseRattingAndComment.objects.filter(course = one_course)

    context = {
        'course':one_course,
         'course_category': all_category,
         'course_rattings' : course_rattings
    }

    if request.method == "POST":
        user = request.user
        
        print("request ", request.POST)
        CourseRattingAndComment.objects.create(
            user = user,
            course = one_course,
            rattings = int(request.POST.get("ratting_number")),
            comment  = request.POST.get("comment")

        )
        context['success'] = "Added Comment Successfully"
        return render(request,'course_details.html',context)
    
    return render(request,'course_details.html',context)





def recommendation(request):
    df = pd.DataFrame(list(CourseRattingAndComment.objects.all().values('user', 'course', 'ratings')))
    print("pandas df",df)
    X, user_mapper, course_mapper, user_inv_mapper, course_inv_mapper = create_matrix(df)
    print(user_mapper)

    def find_similar_movies(course_id, X, k, metric='cosine', show_distance=False):
	
        neighbour_ids = []
        
        course_ind = course_mapper[course_id]
        course_vec = X[course_ind]
        k+=1
        kNN = NearestNeighbors(n_neighbors=k, algorithm="brute", metric=metric)
        kNN.fit(X)
        course_vec = course_vec.reshape(1,-1)
        print("course vec",course_vec)
        neighbour = kNN.kneighbors(course_vec, return_distance=show_distance)
        for i in range(0,k):
            n = neighbour.item(i)
            neighbour_ids.append(course_inv_mapper[n])
        neighbour_ids.pop(0)
        return neighbour_ids


    movie_id = 1

    similar_ids = find_similar_movies(movie_id, X, k=0.3)

    print(similar_ids)


    

    # print(df)
    return render(request,'recommendation.html')




