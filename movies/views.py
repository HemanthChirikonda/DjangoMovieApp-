from django.shortcuts import redirect, render
from movies.models import Movie
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
        except Exception as e:
            print(e)
            pass
          
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
        except Exception as e:
            pass
    return redirect('/')