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
    #lab6
    path('search/', views.search, name="books.search"), 
    path('simple/query', views.simple_query, name="simple_query"), 
    path('complex/query', views.complex_query, name="complex_query"), 
    path('lab8/task1', views.lab8_task1, name="lab8_task1"), 
    path('lab8/task2', views.lab8_task2, name="lab8_task2"), 
    path('lab8/task3', views.lab8_task3, name="lab8_task3"), 
    path('lab8/task4', views.lab8_task4, name="lab8_task4"), 
    path('lab8/task5', views.lab8_task5, name="lab8_task5"), 
    path('lab9/task1', views.lab9_task1, name="lab9_task1"), 
    path('lab9/task2', views.lab9_task2, name="lab9_task2"),
    path('lab9/task3', views.lab9_task3, name="lab9_task3"),
    path('lab9/task4', views.lab9_task4, name="lab9_task4"),
    #part1 lab 10
    path('lab9_part1/listbooks', views.lab9_part1_listbooks, name='lab9_part1_listbooks'),
    path('lab9_part1/addbook', views.lab9_part1_addbook, name='lab9_part1_addbook'),
    path('lab9_part1/editbook/<int:id>', views.lab9_part1_editbook, name='lab9_part1_editbook'),
    path('lab9_part1/deletebook/<int:id>', views.lab9_part1_deletebook, name='lab9_part1_deletebook'),
    # part2
    path('lab9_part2/listbooks', views.lab9_part2_listbooks, name='lab9_part2_listbooks'),
    path('lab9_part2/addbook', views.lab9_part2_addbook, name='lab9_part2_addbook'),
    path('lab9_part2/editbook/<int:id>', views.lab9_part2_editbook, name='lab9_part2_editbook'),
    path('lab9_part2/deletebook/<int:id>', views.lab9_part2_deletebook, name='lab9_part2_deletebook'),

]

