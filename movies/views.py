from django.shortcuts import redirect, render
from movies.models import Movie
from django.contrib import messages
# Create your views here.

def home_page(request):
    query_string= str(request.GET.get('query',''))
    search_results= Movie.objects.filter(name__icontains=query_string)
    content_for_FrontEnd= {
        'search_results':search_results
    }
    return render(request,"movie/movies_staff.html", content_for_FrontEnd)

def create(request):
    if request.method == "POST":
        try:
            responce = Movie.objects.create(
                 name= request.POST.get('name'),
                 picture= request.POST.get('picture'),
                 rating= int(request.POST.get('rating')),
                 notes= request.POST.get('notes'))
            messages.success(request,"New movie added: {}".format(request.POST.get('name')))
        except Exception as e:
            messages.warning(request,"Got an error when you trying to add a movie {}".format(e))
          
    return redirect('/')

def edit(request,movie_id):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'picture': request.POST.get('picture'),
            'rating': int(request.POST.get('rating')),
            'notes': request.POST.get('notes')
        }
        try:
            movie_obj = Movie.objects.get(id=movie_id)
            movie_obj.name = data.get('name')
            movie_obj.picture = data.get('picture')
            movie_obj.rating = data.get('rating')
            movie_obj.notes = data.get('notes')
            movie_obj.save()
            messages.success(request,"Movie updated: {}".format(data.get('name')))       
        except Exception as e:
            messages.warning(request, f"Got an error when trying to update a movie. {data.get('name')}")
    return redirect('/')

def delete(request,movie_id):
    try:
        movie_obj = Movie.objects.get(id=movie_id)
        movie_name= movie_obj.name
        movie_obj.delete()
        messages.success(request,"Movie deleted {}" .format(movie_name))       
    except Exception as e:
        messages.warning(request, f"Got an error when trying to delete a movie. {movie_name}")
    return redirect('/')