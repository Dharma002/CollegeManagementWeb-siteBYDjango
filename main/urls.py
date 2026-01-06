from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('departments/', views.departments, name='departments'),
    path('admission/', views.admission, name='admission'),
    
    path('departments/arts/', views.arts, name='arts'),
    path('departments/biology/', views.biology, name='biology'),
    path('departments/maths/', views.maths, name='maths'),
    path('departments/agriculture/', views.agriculture, name='agriculture'),
    path('notices/', views.notices, name='notices'),
    path('faculty/', views.faculty, name='faculty'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('student-result/', views.student_result, name='student_result'),
    path('student/login/', views.student_login, name='student_login'),
    path('student/logout/', views.student_logout, name='student_logout'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/complete-profile/', views.complete_profile, name='complete_profile'),


]
