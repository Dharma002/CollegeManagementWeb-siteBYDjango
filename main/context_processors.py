from .models import StudentProfile

def student_profile_status(request):
    if request.user.is_authenticated:
        return {
            'has_student_profile': StudentProfile.objects.filter(
                user=request.user
            ).exists()
        }
    return {
        'has_student_profile': False
    }
