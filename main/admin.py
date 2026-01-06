from django.contrib import admin
from .models import Admission,Notice,Faculty,Gallery,Contact,Student, Result,StudentProfile

# Register your models here.
@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_class', 'department', 'phone', 'created_at')
    search_fields = ('name', 'mobile')
    
    
    @admin.register(Notice)
    class NoticeAdmin(admin.ModelAdmin):
       list_display = ('title', 'is_important', 'created_at')
       list_filter = ('is_important',)
       search_fields = ('title',)

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'department', 'experience')
    list_filter = ('department',)
    search_fields = ('name', 'subject')
    
    
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')    
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at') 
    
    
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'name', 'student_class', 'department')
    search_fields = ('roll_no', 'name')

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'marks', 'max_marks')
    search_fields = ('student__roll_no',)       
    
@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'roll_no', 'student_class', 'department')    