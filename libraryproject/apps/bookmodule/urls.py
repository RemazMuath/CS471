from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.links, name="books.links"), 
    path('html5/text/formatting/', views.formatting, name="books.formatting"), 
    path('html5/listing/', views.listing, name="books.listing"), 
    path('html5/tables/', views.tables, name="books.tables"), 
    path('search/', views.search, name="books.search"), 
    path('simple/query', views.simple_query, name="simple_query"), 
    path('complex/query', views.complex_query, name="complex_query"), 

]

