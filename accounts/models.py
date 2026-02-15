from django.db import models
from django.contrib.auth.models import User

class ApplicantProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='applicant_profile')
    otasining_ismi = models.CharField('Otasining ismi', max_length=100, blank=True)
    tugilgan_sana = models.DateField('Tug\'ilgan sana', null=True, blank=True)
    telefon = models.CharField('Telefon raqami', max_length=20, blank=True)
    manzil = models.TextField('Yashash manzili', blank=True)
    passport_seriya = models.CharField('Passport seriya va raqami', max_length=20, blank=True)
    rasm = models.ImageField('Rasm', upload_to='applicant_photos/', blank=True, null=True)
    yaratilgan_sana = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Abituriyent profili'
        verbose_name_plural = 'Abituriyent profillari'

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name}"

class StaffProfile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('reviewer', 'Tekshiruvchi'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_profile')
    lavozim = models.CharField('Lavozimi', max_length=100, blank=True)
    role = models.CharField('Roli', max_length=20, choices=ROLE_CHOICES, default='reviewer')
    telefon = models.CharField('Telefon raqami', max_length=20, blank=True)
    yaratilgan_sana = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Xodim profili'
        verbose_name_plural = 'Xodim profillari'

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name} - {self.lavozim}"
