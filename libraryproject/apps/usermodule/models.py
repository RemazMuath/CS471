from django.db import models


#lab8
# Address model
class Address(models.Model):
    city = models.CharField(max_length=100)


# Student model
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=20)
    address = models.ForeignKey(Address,on_delete=models.SET_NULL, null=True)#here error must add , null=True _from terminal



#lab9
#python manage.py makemigrations usermodule
#python manage.py migrate

class Card(models.Model):
    card_number = models.IntegerField(default=20)

#one dept have many student and each student have one dep only so its --ONE TO MANY -- so we use foreign key in student model
class Department(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField()
    
class Student2(models.Model):
    name = models.CharField(max_length=100)
    card = models.OneToOneField(Card, on_delete=models.PROTECT) #protect the deletion of card
    department = models.ForeignKey(Department,on_delete=models.CASCADE) #using cascade to make all students deleted automatically..
    course = models.ManyToManyField(Course)#so many student have many cources MANY TO MANY    
    
    
    