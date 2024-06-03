from .views import send_email
from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    
    path('login/', views.login, name='login'),  # Login page
    path('index/', views.index, name='index'),  # Regular index page
     path('registration/', views.registration_form, name='registration_form'),
     path('registration/success/', views.registration_success, name='registration_success'),
    path('send_email/', send_email, name='send_email'),
     path('take_Attendance/', views.take_Attendance, name='take_Attendance'),
    path('attendance_success/', views.attendance_success, name='attendance_success'),
  path('add_student/', views.add_student, name='add_student'),
  path('view-all/', views.view_all, name='view_all'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='reset_password.html'), name='reset_password'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(template_name='reset_password_done.html'), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset_password_confirm.html'), name='password_reset_confirm'),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'), name='password_reset_complete'),
    # other URLs
]
