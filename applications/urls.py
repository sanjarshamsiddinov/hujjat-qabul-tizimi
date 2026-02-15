from django.urls import path
from . import views

urlpatterns = [
    # Abituriyent
    path('ariza/yaratish/', views.create_application, name='create_application'),
    path('ariza/<int:pk>/', views.application_detail, name='application_detail'),
    path('ariza/<int:pk>/hujjatlar/', views.upload_documents, name='upload_documents'),
    path('ariza/<int:pk>/chop-etish/', views.print_application, name='print_application'),
    path('hujjat/<int:pk>/ochirish/', views.delete_document, name='delete_document'),

    # Public
    path('ariza-holati/', views.check_status, name='check_status'),

    # Xodim
    path('xodim/dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('xodim/arizalar/', views.staff_applications_list, name='staff_applications_list'),
    path('xodim/arizalar/export/', views.export_applications_excel, name='export_applications'),
    path('xodim/ariza/<int:pk>/', views.staff_application_detail, name='staff_application_detail'),
    path('xodim/hujjat/<int:pk>/tekshirish/', views.staff_review_document, name='staff_review_document'),
    path('xodim/fakultetlar/', views.staff_faculties, name='staff_faculties'),
    path('xodim/yonalishlar/', views.staff_specialties, name='staff_specialties'),
    path('xodim/hujjat-turlari/', views.staff_document_types, name='staff_document_types'),

    # API
    path('api/stats/', views.api_stats, name='api_stats'),
]
