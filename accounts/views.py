from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ApplicantRegistrationForm, LoginForm, ApplicantProfileForm
from .models import ApplicantProfile

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = ApplicantRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            ApplicantProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz!")
            return redirect('dashboard')
    else:
        form = ApplicantRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Tizimga muvaffaqiyatli kirdingiz!")
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "Tizimdan chiqdingiz.")
    return redirect('home')

@login_required
def profile_view(request):
    try:
        profile = request.user.applicant_profile
    except ApplicantProfile.DoesNotExist:
        profile = ApplicantProfile.objects.create(user=request.user)
    
    if request.method == 'POST':
        form = ApplicantProfileForm(request.POST, request.FILES, instance=profile)
        form.fields['first_name'].initial = request.user.first_name
        form.fields['last_name'].initial = request.user.last_name
        form.fields['email'].initial = request.user.email
        if form.is_valid():
            form.save()
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.email = form.cleaned_data['email']
            request.user.save()
            messages.success(request, "Profil muvaffaqiyatli yangilandi!")
            return redirect('profile')
    else:
        form = ApplicantProfileForm(instance=profile)
        form.fields['first_name'].initial = request.user.first_name
        form.fields['last_name'].initial = request.user.last_name
        form.fields['email'].initial = request.user.email
    return render(request, 'accounts/profile.html', {'form': form, 'profile': profile})
