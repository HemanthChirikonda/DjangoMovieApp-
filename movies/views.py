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