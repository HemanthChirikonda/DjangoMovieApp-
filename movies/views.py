from django.shortcuts import render
from movies.models import Movie
# Create your views here.

def home_page(request):
    query_string= str(request.GET.get('query',''))
    search_results= Movie.objects.filter(name__icontains=query_string)
    content_for_FrontEnd= {
        'search_results':search_results
    }
    return render(request,"movie/movies_staff.html", content_for_FrontEnd)