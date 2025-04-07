from django.db import models

# Address model
class Address(models.Model):
    city = models.CharField(max_length=100)


# Student model
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=20)
    address = models.ForeignKey(Address,on_delete=models.SET_NULL, null=True)#here error must add , null=True _from terminal



