from .views import home_page, create
from django.urls import path


urlpatterns=[
    path('', home_page, name="home_page" ),
    path('create/', create, name='create')
]