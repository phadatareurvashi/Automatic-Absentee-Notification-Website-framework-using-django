# forms.py

from django import forms
from .models import Registration,Student
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'

class LoginForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

from django.contrib.auth.forms import PasswordResetForm

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email'}))


from .models import Attendance

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'status']

    def __init__(self, *args, **kwargs):
        super(AttendanceForm, self).__init__(*args, **kwargs)
        self.fields['student'].label = "Student"
        self.fields['date'].label = "Date"
        self.fields['status'].label = "Attendance Status"

        # Customize the queryset for the student field to include roll number and name
        self.fields['student'].queryset = Student.objects.all().values_list('id', 'user__first_name', 'user__last_name', 'roll_number')
        self.fields['student'].widget = forms.Select(choices=[(id, f'{first_name} {last_name} - Roll: {roll_number}') for id, first_name, last_name, roll_number in self.fields['student'].queryset])

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll']