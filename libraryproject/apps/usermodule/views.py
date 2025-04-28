from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from .models import Address, Student,Photos,Student22,Address2
from .forms import StudentForm,PhotoForm,Student22Form

def lab8_task7(request):
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'usermodule/lab8_task7.html', {'cities': cities})

# lab 11 
def list_students(request):
    students = Student.objects.all()
    return render(request, 'usermodule/list_students.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save() #to add
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'usermodule/add_edit_student.html', {'form': form})

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

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('list_students')
    return render(request, 'usermodule/delete_students.html', {'student': student})

#task2
def Lab11_task2(request):
    students = Student22.objects.prefetch_related('addresses').all()
    return render(request, 'usermodule/Lab11_task2.html', {'students': students})

def add_student_address(request):
    if request.method == 'POST':
        form = Student22Form(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('Lab11_task2') 
    else:
        form = Student22Form()
    return render(request, 'usermodule/add_edit_student_address.html', {'form': form})

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