from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# --- Existing Models ---

class Admission(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=10)
    department = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Notice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_important = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

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

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Student(models.Model):
    roll_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=10)
    department = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.roll_no} - {self.name}"

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()
    max_marks = models.IntegerField(default=100)

    def __str__(self):
        return f"{self.student.roll_no} - {self.subject}"

# --- Updated StudentProfile Model ---

class StudentProfile(models.Model):
    CLASS_CHOICES = [
        ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),
        ('10', '10'), ('11', '11'), ('12', '12'),
    ]
    DEPARTMENT_CHOICES = [
        ('arts', 'Arts'), ('biology', 'Biology'),
        ('maths', 'Maths'), ('agriculture', 'Agriculture'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Signup ke waqt roll_no nahi hota, isliye null=True, blank=True rakha hai
    roll_no = models.CharField(max_length=20, unique=True, null=True, blank=True)
    student_class = models.CharField(max_length=10, choices=CLASS_CHOICES, null=True, blank=True)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.user.username

# --- SIGNALS FOR AUTOMATION ---
# Jaise hi naya User register hoga, ye signal uske liye automatically profile bana dega

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        StudentProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.studentprofile.save()