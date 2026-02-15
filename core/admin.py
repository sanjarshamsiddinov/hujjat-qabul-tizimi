from django.contrib import admin
from .models import University, Faculty, Specialty, AdmissionCampaign


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'kodi', 'turi', 'viloyat', 'faol', 'yaratilgan_sana']
    list_filter = ['turi', 'viloyat', 'faol']
    search_fields = ['nomi', 'kodi']
    list_per_page = 50


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'kodi', 'universitet', 'faol', 'yaratilgan_sana']
    list_filter = ['faol', 'universitet']
    search_fields = ['nomi', 'kodi']


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'kodi', 'fakultet', 'talim_turi', 'kvota', 'faol']
    list_filter = ['fakultet', 'talim_turi', 'faol']
    search_fields = ['nomi', 'kodi']


@admin.register(AdmissionCampaign)
class AdmissionCampaignAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'yil', 'boshlanish_sanasi', 'tugash_sanasi', 'faol']
    list_filter = ['faol', 'yil']
