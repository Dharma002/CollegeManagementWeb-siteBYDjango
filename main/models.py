from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Admission(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=10)
    department = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    #Contact Models
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
    #Notice Model 
class Notice(models.Model):
       title = models.CharField(max_length=200)
       description = models.TextField()
       is_important = models.BooleanField(default=False)
       created_at = models.DateTimeField(auto_now_add=True)

       def __str__(self):
         return self.title
     
     #Faculty Model
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    qualification = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='faculty/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
    #Gallery Model
class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

#Student Models
class Student(models.Model):
    roll_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=10)
    department = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.roll_no} - {self.name}"
    
    #Results Models
class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()
    max_marks = models.IntegerField(default=100)

    def __str__(self):
        return f"{self.student.roll_no} - {self.subject}"

   #Student_Profile Models

class StudentProfile(models.Model):

    CLASS_CHOICES = [
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    ]

    DEPARTMENT_CHOICES = [
        ('arts', 'Arts'),
        ('biology', 'Biology'),
        ('maths', 'Maths'),
        ('agriculture', 'Agriculture'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=20, unique=True)
    student_class = models.CharField(
        max_length=10,
        choices=CLASS_CHOICES
    )
    department = models.CharField(
        max_length=50,
        choices=DEPARTMENT_CHOICES
    )

    def __str__(self):
        return self.user.username    
    
    
    
