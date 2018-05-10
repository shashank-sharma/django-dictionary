from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from . import views

urlpatterns = [
    re_path(r'^(?P<key>[a-z]{1})$', views.letter, name='letter'),
    path('', views.home, name='home'),
    path('add-word', views.add_word),
    path('delete-word', views.delete_word),
    path('search-word', views.search_word),
    path('get-word', views.get_word),
]