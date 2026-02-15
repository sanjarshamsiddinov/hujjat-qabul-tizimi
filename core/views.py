from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import AdmissionCampaign, University, Faculty, Specialty
from applications.models import Application

User = get_user_model()

def home_view(request):
    active_campaign = AdmissionCampaign.objects.filter(faol=True).first()
    universities = University.objects.filter(faol=True)
    faculties = Faculty.objects.filter(faol=True)
    context = {
        'active_campaign': active_campaign,
        'universities': universities,
        'faculties': faculties,
        'universities_count': universities.count(),
        'faculties_count': faculties.count(),
        'specialties_count': Specialty.objects.filter(faol=True).count(),
        'applicants_count': User.objects.filter(applicant_profile__isnull=False).count(),
        'applications_count': Application.objects.count(),
    }
    return render(request, 'core/home.html', context)

@login_required
def dashboard_view(request):
    # Check if user is staff
    if hasattr(request.user, 'staff_profile'):
        return redirect('staff_dashboard')
    # Applicant dashboard
    try:
        profile = request.user.applicant_profile
    except:
        from accounts.models import ApplicantProfile
        profile = ApplicantProfile.objects.create(user=request.user)
    
    applications = Application.objects.filter(abituriyent=request.user).order_by('-yaratilgan_sana')
    context = {
        'profile': profile,
        'applications': applications,
        'total_count': applications.count(),
        'in_process_count': applications.filter(holat__in=['yangi', 'korib_chiqilmoqda']).count(),
        'accepted_count': applications.filter(holat='qabul_qilindi').count(),
        'rejected_count': applications.filter(holat='rad_etildi').count(),
    }
    return render(request, 'core/applicant_dashboard.html', context)
