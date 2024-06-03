from django.db import models
from django.contrib.auth.models import User


class Registration(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)  # Assuming you're storing phone numbers as strings
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

def __str__(self):
    return self.name 


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.CharField(max_length=20, unique=True)
    parent_email = models.EmailField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.name

    @classmethod
    def arrange_roll_numbers(cls):
        students = cls.objects.order_by('id')
        for i, student in enumerate(students, start=1):
            student.roll = str(i)
            student.save()



    



class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=(('present', 'Present'), ('absent', 'Absent')))
def __str__(self):
    return self.name    


