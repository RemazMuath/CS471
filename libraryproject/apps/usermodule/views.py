from django.shortcuts import render
from django.db.models import Count
from .models import Address

# Create your views here.

def lab8_task7(request):
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'usermodule/lab8_task7.html', {'cities': cities})