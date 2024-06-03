from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm,StudentForm
from django.contrib.auth.forms import PasswordResetForm
from .models import Student
from .forms import LoginForm
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from datetime import date
from .utils import send_email_to_client

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request, 'login.html')

def registration_form(request):
    # Your signup logic here
    return render(request, 'registration_form.html')

def registration_success(request):
    return render(request, 'registration_success.html')

# views.py

def registration_form(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
            # Redirect to a success page or perform other actions
    else:
        form = RegistrationForm()
    return render(request, 'registration_form.html', {'form': form})


# views.py




# def send_email_to_parents(request):
def send_email(request):  
    parent_emails = ['phadatareakshada87@gmail.com', 'phadataresanjay756@gmail.com']  # Example list of parent email addresses
    message = "Dear parents, \n\nThis is to inform you about the Absentee of your child. \n\nRegards, \nTrinity Academy of Engineering,Pune"

    try:
        send_mail(
            'Important Message from School',
            message,
            'urvashiphadatare26@example.com',  # Sender's email address
            parent_emails,
            fail_silently=False,
        )
        return render(request, 'success.html')  # Render a success page after sending the email
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})  # Render an error page if there's an exception




def forgot_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            return render(request, 'reset_password_done.html')
    else:
        form = PasswordResetForm()
    return render(request, 'forgot_password.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('index')  # Redirect to dashboard or any other page
#         else:
#             return render(request, 'notification/login.html', {'error_message': 'Invalid username or password'})
#     return render(request, 'notification/login.html')

from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or any other page
                return redirect('index')
            else:
                # Authentication failed, display an error message
                error_message = "Invalid email or password."
    else:
        form = LoginForm()
        error_message = None

    return render(request, 'login.html', {'form': form, 'error_message': error_message})

def take_Attendance(request):
    return render(request, 'take_Attendance.html')

def view_all(request):
    return render(request, 'view_all.html')



from .forms import AttendanceForm
def take_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save()
            if attendance.status == 'absent':
                send_absentee_notification(attendance.student)
            return redirect('attendance_success')  # Redirect to a success page
    else:
        form = AttendanceForm()
    return render(request, 'attendance/take_attendance.html', {'form': form})

def send_absentee_notification(student):
    # Code to send notification to parent's email
    parent_email = student.user.email
    subject = 'Attendance Notification'
    message = f'Dear Parent, Your child {student.user.first_name} {student.user.last_name} was absent today.'
    send_mail(subject, message, 'your_email@example.com', [parent_email])

def attendance_success(request):
    return render(request, 'attendance/attendance_success.html')

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the index page after adding the student
    else:
        form = StudentForm()
    
    students = Student.objects.all()  # Retrieve all students from the database
    return render(request, 'add_student.html', {'form': form, 'students': students})
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the index page after adding the student
        else:
          form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def send_email(request):
    send_email_to_client()
    return redirect('/')

def mark_attendance(request):
    # Your attendance marking logic here
    absent_students = get_absent_students()  # Get absent students list

    # Extract parent emails of absent students
    absentee_emails = [student.parent_email for student in absent_students]

    # Send email notifications to parents of absent students
    send_email_to_client(absentee_emails)

    return render(request, 'index.html', {'absent_students': absent_students})