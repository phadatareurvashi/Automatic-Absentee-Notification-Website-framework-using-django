from django.contrib import admin
from .models import Registration,Attendance,Student

# Register your models here.
admin.site.register(Registration)
admin.site.register(Attendance)
admin.site.register(Student)