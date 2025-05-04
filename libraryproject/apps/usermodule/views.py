from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from .models import Address, Student,Photos,Student22,Address2
from .forms import StudentForm,PhotoForm,Student22Form
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required


def lab8_task7(request):
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'usermodule/lab8_task7.html', {'cities': cities})

# lab 11 
@login_required()  # redirect to login if user is not authenticated
def list_students(request):
    students = Student.objects.all()
    return render(request, 'usermodule/list_students.html', {'students': students})

@login_required()
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save() #to add
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'usermodule/add_edit_student.html', {'form': form})

@login_required()
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'usermodule/add_edit_student.html', {'form': form})

@login_required()
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('list_students')
    return render(request, 'usermodule/delete_students.html', {'student': student})

#task2
@login_required()
def Lab11_task2(request):
    students = Student22.objects.prefetch_related('addresses').all()
    return render(request, 'usermodule/Lab11_task2.html', {'students': students})

@login_required()
def add_student_address(request):
    if request.method == 'POST':
        form = Student22Form(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('Lab11_task2') 
    else:
        form = Student22Form()
    return render(request, 'usermodule/add_edit_student_address.html', {'form': form})

@login_required()
def edit_student_address(request, id):
    student = get_object_or_404(Student22, id=id)
    if request.method == 'POST':
        form = Student22Form(request.POST, instance=student)
        if form.is_valid():
            form.save() 
            return redirect('Lab11_task2')  
    else:
        form = Student22Form(instance=student)
    return render(request, 'usermodule/add_edit_student_address.html', {'form': form})

@login_required()
def delete_student2(request, id):
    student = get_object_or_404(Student22, id=id) 
    
    if request.method == 'POST':
        student.delete() 
        return redirect('Lab11_task2') 
    
    return render(request, 'usermodule/delete_student2.html', {'student': student}) 

#task 3 
def photo_list(request):
    photos = Photos.objects.all()
    return render(request, 'usermodule/photo_list.html', {'photos': photos})

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES) #using request.FILES to receive uploaded files..
        if form.is_valid():
            form.save()
            return redirect('photo_list')  #redirect after success
    else:
        form = PhotoForm()
    return render(request, 'usermodule/upload_photo.html', {'form': form})

#lab12

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')
        user = User.objects.create_user(username=username, password=password)
        messages.success(request, "You have successfully registered")
        return redirect('list_students')
    return render(request, 'usermodule/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('list_students')  
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'usermodule/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('login')
