from django import forms
from .models import Student,Photos,Student22,Address2

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']


class Student22Form(forms.ModelForm):
    class Meta:
        model = Student22
        fields = ['name', 'age', 'addresses']
       
    addresses = forms.ModelMultipleChoiceField(
        queryset=Address2.objects.all(),  
        widget=forms.CheckboxSelectMultiple,  
        required=False 
    )

#task3
class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ['title', 'image']