from django.contrib import admin
from .models import ApplicantProfile, StaffProfile

@admin.register(ApplicantProfile)
class ApplicantProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'passport_seriya', 'telefon', 'yaratilgan_sana']
    search_fields = ['user__first_name', 'user__last_name', 'passport_seriya']

@admin.register(StaffProfile)
class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'lavozim', 'role', 'telefon']
    list_filter = ['role']
