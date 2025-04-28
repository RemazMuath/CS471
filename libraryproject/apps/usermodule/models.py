from django.db import models


#lab8
# Address model
class Address(models.Model):
    city = models.CharField(max_length=100)
    def __str__(self):
        return self.city


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
    
    
#lab 11 task2 
# Address model 2
class Address2(models.Model):
    city = models.CharField(max_length=100)
    def __str__(self):
        return self.city


# Student model
class Student22(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=20)
    addresses = models.ManyToManyField(Address2)  # Many-to-Many here is the diffrence !!
    def __str__(self):
        return self.name
    

#python manage.py makemigrations
#python manage.py migrate

#task 3
class Photos(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.title
