from .views import edit, home_page, create
from django.urls import path


urlpatterns=[
    path('', home_page, name="home_page" ),
    path('create/', create, name='create'),
    path('edit/<str:movie_id>',edit,name='edit')
]