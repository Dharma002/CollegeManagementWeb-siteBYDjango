from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Admission,Notice,Faculty,Gallery,Contact,Student, Result,StudentProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import StudentProfileForm



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def departments(request):
    return render(request, 'departments.html')

def admission(request):
    if request.method == "POST":
        Admission.objects.create(
            name=request.POST.get('name'),
            student_class=request.POST.get('student_class'),
            department=request.POST.get('department'),
            phone=request.POST.get('mobile'),
            address=request.POST.get('address')
        )

        messages.success(request, "Admission enquiry submitted successfully!")
        return redirect('admission')

    return render(request, 'admission.html')


def student_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('student_dashboard')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'student_login.html')


def student_logout(request):
    logout(request)
    return redirect('student_login')


@login_required
def student_dashboard(request):
    try:
        profile = StudentProfile.objects.get(user=request.user)
    except StudentProfile.DoesNotExist:
        return redirect('complete_profile')  # force user to fill details

    return render(request, 'student/dashboard.html', {'profile': profile})

@login_required
def complete_profile(request):
    if StudentProfile.objects.filter(user=request.user).exists():
        return redirect('student_dashboard')

    if request.method == "POST":
        form = StudentProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('student_dashboard')
    else:
        form = StudentProfileForm()

    return render(request, 'student/complete_profile.html', {'form': form})



#Contact views 
def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            message=request.POST.get('message')
        )
        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')

    return render(request, 'contact.html')


#Studens and results Views 
def student_result(request):
    results = None
    student = None

    if request.method == "POST":
        roll_no = request.POST.get('roll_no')
        student = Student.objects.filter(roll_no=roll_no).first()

        if student:
            results = Result.objects.filter(student=student)
        else:
            messages.error(request, "Invalid Roll Number")

    return render(request, 'student_result.html', {
        'student': student,
        'results': results
    })



def arts(request):
    return render(request, 'departments/arts.html')

def biology(request):
    return render(request, 'departments/biology.html')

def maths(request):
    return render(request, 'departments/maths.html')

def agriculture(request):
    return render(request, 'departments/agriculture.html')

def notices(request):
    all_notices = Notice.objects.order_by('-created_at')
    return render(request, 'notices.html', {'notices': all_notices})

def faculty(request):
    teachers = Faculty.objects.all()
    return render(request, 'faculty.html', {'teachers': teachers})


def gallery(request):
    photos = Gallery.objects.all().order_by('-created_at')
    return render(request, 'gallery.html', {'photos': photos})

