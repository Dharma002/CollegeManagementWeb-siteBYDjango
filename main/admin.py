from django.contrib import admin
from .models import Admission, Notice, Faculty, Gallery, Contact, Student, Result, StudentProfile

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_class', 'department', 'phone', 'created_at')
    search_fields = ('name', 'phone') # 'mobile' ki jagah 'phone' kyunki model mein phone hai
    list_filter = ('department', 'student_class')

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
    search_fields = ('title',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email')
    readonly_fields = ('created_at',) # Isse admin contact message ko edit nahi kar payega, sirf padh sakega

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'name', 'student_class', 'department')
    search_fields = ('roll_no', 'name')
    list_filter = ('student_class', 'department')

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('get_roll', 'student', 'subject', 'marks', 'max_marks')
    search_fields = ('student__roll_no', 'student__name')
    
    # Isse Result table mein Student ka Roll Number bhi dikhega
    def get_roll(self, obj):
        return obj.student.roll_no
    get_roll.short_description = 'Roll No'

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'roll_no', 'student_class', 'department')
    search_fields = ('user__username', 'roll_no')
    list_filter = ('student_class', 'department')