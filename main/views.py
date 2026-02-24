from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Admission,Notice,Faculty,Gallery,Contact,Student, Result,StudentProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import StudentProfileForm
from django.contrib.auth.forms import UserCreationForm
import google.generativeai as genai
from django.http import JsonResponse



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





# AI Configuration (Free key Google AI Studio se lein)
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Admission,Notice,Faculty,Gallery,Contact,Student, Result,StudentProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import StudentProfileForm
import google.generativeai as genai
from django.http import JsonResponse



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

def student_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully! Ab login karein.")
            return redirect('student_login')
    else:
        form = UserCreationForm()
    return render(request, 'student/register.html', {'form': form})


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







# API Key pakka check kar lena bhai
genai.configure(api_key="AIzaSyD38hrqRZ5eCI54C1JX6CWsCE-WpofXxTs")

def ai_assistant(request):
    user_query = request.GET.get('msg', '').lower()
    reply = ""

    # 1. Gallery/Photos Automation (Database se images nikalna)
    if any(word in user_query for word in ["photo", "gallery", "image", "tasveer", "pic"]):
        photos = Gallery.objects.all().order_by('-created_at')[:3]  # Latest 3 photos
        if photos.exists():
            reply = "Sure, man! Here are some glimpses of SPIC College. You can see more photos on the 'Gallery' page.<br><br>"
            for p in photos:
                # Yahan hum responsive image tag bhej rahe hain
                reply += f'<img src="{p.image.url}" style="width:100%; border-radius:15px; margin-bottom:12px; border:2px solid #fff; shadow: 0 4px 8px rgba(0,0,0,0.1);">'
            return JsonResponse({'reply': reply})
        else:
            return JsonResponse({'reply': "Brother, there are no photos in the gallery yet. Will be uploaded soon!"})

    # 2. Faculty Automation (Database se Teacher ki info)
    elif any(word in user_query for word in ["teacher", "faculty", "sir", "madam", "sirji", "guru"]):
        teachers = Faculty.objects.all()
        if teachers.exists():
            reply = "<b>Experienced Faculty of our College:</b><br><br>"
            for t in teachers:
                # Agar teacher ki photo hai toh use dikhao, nahi toh default icon
                photo_url = t.photo.url if t.photo else "/static/images/default-teacher.png"
                
                reply += f'''
                <div style="background: #fff; border-radius: 12px; padding: 10px; margin-bottom: 15px; border: 1px solid #ddd; text-align: center; box-shadow: 0 2px 5px rgba(0,0,0,0.05);">
                    <img src="{photo_url}" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; border: 3px solid #007bff; margin-bottom: 8px;">
                    <div style="font-weight: bold; color: #007bff; font-size: 16px;">{t.name}</div>
                    <div style="font-size: 13px; color: #555;">{t.subject} Specialist</div>
                    <div style="font-size: 12px; color: #888;">{t.experience} Experience</div>
                </div>
                '''
            reply += "Do you want to know more about them?"
            return JsonResponse({'reply': reply})
        else:
            return JsonResponse({'reply': "The faculty list is currently being updated."})

    # 3. Latest Notice Automation
    elif "notice" in user_query or "update" in user_query:
        latest_notices = Notice.objects.order_by('-created_at')[:3]
        if latest_notices.exists():
            notice_text = "<b>Latest Updates:</b><br>"
            for n in latest_notices:
                notice_text += f"📢 {n.title}: {n.description[:60]}...<br>"
            return JsonResponse({'reply': notice_text})
        else:
            return JsonResponse({'reply': "There is no new notice yet."})

    # 4. Result/Department Logic
    elif "result" in user_query or "marks" in user_query:
        return JsonResponse({'reply': "To check the result, go to the 'Student Result' page and enter your roll number."})

    # 5. Gemini AI Fallback
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(f"User query: {user_query}. Respond in friendly Hinglish for SPIC College.")
        reply = response.text
    except Exception:
        reply = "I'm a SPIC Assistant. You can ask me about admissions, faculty, notices, or the gallery."

    return JsonResponse({'reply': reply})

