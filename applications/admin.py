from django.contrib import admin
from .models import DocumentType, Application, Document

@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'majburiy', 'tartib']
    list_filter = ['majburiy']
    list_editable = ['tartib']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'abituriyent', 'yonalish', 'qabul_davri', 'holat', 'yaratilgan_sana']
    list_filter = ['holat', 'qabul_davri', 'yonalish__fakultet']
    search_fields = ['abituriyent__first_name', 'abituriyent__last_name']
    readonly_fields = ['yaratilgan_sana', 'yangilangan_sana']

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['hujjat_turi', 'ariza', 'holat', 'yuklangan_sana', 'tekshirgan']
    list_filter = ['holat', 'hujjat_turi']
    readonly_fields = ['yuklangan_sana']
