from django.shortcuts import render
from notification.models import  Registration,Student,Attendance

def index(request):
    students = Student.objects.all()
    Student.arrange_roll_numbers()
    return render(request, 'index.html', {'students': students})
    


