from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_page, name='books_page')
]