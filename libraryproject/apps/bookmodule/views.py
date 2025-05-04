from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Book
from django.db.models import Q ,Count, Sum, Avg, Max, Min
#be carefull here it should be apps.usermodule first 
from apps.usermodule.models import *
from .forms import BookForm
# def index(request):
#     return HttpResponse("Hello, world!")

# def index(request):
#     name = request.GET.get("name") or "world!"
#     return render(request, "bookmodule/index.html" , {"name": name})  

def index2(request, val1=0):
    return HttpResponse(f"value1 = {val1}")

# def viewbook(request, bookId):
#     # assume that we have the following books somewhere (e.g. database)
#     book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
#     book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
#     targetBook = None
#     if book1['id'] == bookId: targetBook = book1
#     if book2['id'] == bookId: targetBook = book2
#     context = {'book':targetBook} # book is the variable name accessible by the template
#     return render(request, 'bookmodule/show.html', context)

def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links(request):
    return render(request, 'bookmodule/links.html')

def formatting(request):
    return render(request, 'bookmodule/formatting.html')

def listing(request):
    return render(request, 'bookmodule/listing.html')

def tables(request):
    return render(request, 'bookmodule/tables.html')
#lab6
def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = get_books_list()
        newBooks = []
        
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): 
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
            
            if contained: 
                newBooks.append(item)
                
        return render(request, 'bookmodule/bookList.html', {'books': newBooks})
    
    return render(request, 'bookmodule/search.html')


def get_books_list():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList2.html', {'books':mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList2.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')



def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/lab8_task1.html', {'books': books})

def lab8_task2(request):
    books = Book.objects.filter(Q(edition__gt=3) & Q(title__icontains="co") | Q(author__icontains="co"))
    return render(request, 'bookmodule/lab8_task2.html', {'books': books})

def lab8_task3(request):
    books = Book.objects.filter(Q(edition__lte=3) & ((~Q(title__icontains="co")) | (~Q(author__icontains="co"))))
    return render(request, 'bookmodule/lab8_task3.html', {'books': books})

def lab8_task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/lab8_task4.html', {'books': books})

def lab8_task5(request):
   a = Book.objects.aggregate(
        count=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
   return render(request, 'bookmodule/lab8_task5.html', {'a': a})

#lab9
def lab9_task1(request):
    departments = Department.objects.all()  # Capital D

    dep_data = []
    for dep in departments:
        count = dep.student2_set.count() # One-to-Many relation
        dep_data.append({
            'department_name': dep.name,
            'student_count': count,
        })

    return render(request, 'bookmodule/lab9_task1.html', {'departments': dep_data})


def lab9_task2(request):
    course = Course.objects.all()

    course_data = []
    for course in course:
        count = course.student2_set.count() 
        course_data.append({
            'course_title': course.title,
            'student_count': count,
        })

    return render(request, 'bookmodule/lab9_task2.html', {'courses': course_data})


def lab9_task3(request):
    departments = Department.objects.all()

    dep_data = []
    for dep in departments:
        # name of the oldest student (by ID) For each department 
        oldest_student = dep.student2_set.order_by('id').first()
        if oldest_student:
            student_name = oldest_student.name
        else:#in case theres no student
            student_name = "No students in this department"

        dep_data.append({
            'department_name': dep.name,
            'oldest_student_name': student_name,
        })

    return render(request, 'bookmodule/lab9_task3.html', {'departments': dep_data})

def lab9_task4(request):
    departments = (
    Department.objects
    .annotate(student_count=Count('student2'))  # count the students
    .filter(student_count__gt=2)               # dep with greater than 2 student
    .order_by('-student_count')                # - is for the des and without is by default ascending..
     )

    return render(request, 'bookmodule/lab9_task4.html', {'departments': departments})


def lab9_part1_listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab9_part1_listbooks.html', {'books': books})


def lab9_part1_addbook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        
        Book.objects.create(title=title, author=author)
        return redirect('lab9_part1_listbooks')
    return render(request, 'bookmodule/lab9_part1_addbook.html')


def lab9_part1_editbook(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')

        book.save()
        return redirect('lab9_part1_listbooks')
    return render(request, 'bookmodule/lab9_part1_editbook.html', {'book': book})

def lab9_part1_deletebook(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('lab9_part1_listbooks')


# part 2 
# from .forms import BookForm 
def lab9_part2_listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab9_part2_listbooks.html', {'books': books})

def lab9_part2_addbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab9_part2_listbooks')
    else:
        form = BookForm()
    return render(request, 'bookmodule/lab9_part2_addbook.html', {'form': form})

def lab9_part2_editbook(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('lab9_part2_listbooks')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/lab9_part2_editbook.html', {'form': form})

def lab9_part2_deletebook(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
    return redirect('lab9_part2_listbooks')
