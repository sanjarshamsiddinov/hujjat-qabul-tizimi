from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("ro'yxatdan-o'tish/", views.register_view, name='register'),
    path('kirish/', views.login_view, name='login'),
    path('chiqish/', views.logout_view, name='logout'),
    path('profil/', views.profile_view, name='profile'),

    # Password reset
    path('parol-tiklash/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html',
        email_template_name='accounts/password_reset_email.html',
        subject_template_name='accounts/password_reset_subject.txt',
        success_url='/accounts/parol-tiklash/yuborildi/',
    ), name='password_reset'),
    path('parol-tiklash/yuborildi/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html',
    ), name='password_reset_done'),
    path('parol-tiklash/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html',
        success_url='/accounts/parol-tiklash/tayyor/',
    ), name='password_reset_confirm'),
    path('parol-tiklash/tayyor/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html',
    ), name='password_reset_complete'),
]
