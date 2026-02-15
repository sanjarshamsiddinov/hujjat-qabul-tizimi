from django.db import models


class University(models.Model):
    """Oliy ta'lim muassasasi (OTM)"""
    UNIVERSITY_TYPES = [
        ('davlat', 'Davlat OTM'),
        ('xususiy', 'Nodavlat (Xususiy) OTM'),
        ('xorijiy', 'Xorijiy OTM filiali'),
        ('harbiy', 'Harbiy OTM'),
    ]
    nomi = models.CharField('OTM nomi', max_length=300)
    kodi = models.CharField('OTM kodi', max_length=30, unique=True)
    turi = models.CharField('OTM turi', max_length=20, choices=UNIVERSITY_TYPES, default='davlat')
    viloyat = models.CharField('Viloyat / Shahar', max_length=100, blank=True)
    manzil = models.CharField('Manzil', max_length=300, blank=True)
    veb_sayt = models.URLField('Veb-sayt', blank=True)
    tavsif = models.TextField('Tavsif', blank=True)
    faol = models.BooleanField('Faol', default=True)
    yaratilgan_sana = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'OTM (Universitet)'
        verbose_name_plural = 'OTMlar (Universitetlar)'
        ordering = ['turi', 'nomi']

    def __str__(self):
        return self.nomi


class Faculty(models.Model):
    nomi = models.CharField('Fakultet nomi', max_length=200)
    kodi = models.CharField('Fakultet kodi', max_length=20, unique=True)
    universitet = models.ForeignKey(
        University, on_delete=models.CASCADE,
        related_name='fakultetlar', verbose_name='OTM',
        null=True, blank=True
    )
    tavsif = models.TextField('Tavsif', blank=True)
    faol = models.BooleanField('Faol', default=True)
    yaratilgan_sana = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Fakultet'
        verbose_name_plural = 'Fakultetlar'
        ordering = ['nomi']

    def __str__(self):
        return self.nomi


class Specialty(models.Model):
    EDUCATION_TYPE_CHOICES = [
        ('bakalavr', 'Bakalavr'),
        ('magistr', 'Magistratura'),
    ]
    nomi = models.CharField("Yo'nalish nomi", max_length=200)
    kodi = models.CharField("Yo'nalish kodi", max_length=20, unique=True)
    fakultet = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='yonalishlar', verbose_name='Fakultet')
    talim_turi = models.CharField("Ta'lim turi", max_length=20, choices=EDUCATION_TYPE_CHOICES, default='bakalavr')
    kvota = models.PositiveIntegerField('Kvota (o\'rinlar soni)', default=0)
    tavsif = models.TextField('Tavsif', blank=True)
    faol = models.BooleanField('Faol', default=True)

    class Meta:
        verbose_name = "Yo'nalish"
        verbose_name_plural = "Yo'nalishlar"
        ordering = ['fakultet', 'nomi']

    def __str__(self):
        return f"{self.nomi} ({self.get_talim_turi_display()})"


class AdmissionCampaign(models.Model):
    nomi = models.CharField('Qabul davri nomi', max_length=200)
    yil = models.PositiveIntegerField('Yil')
    boshlanish_sanasi = models.DateField('Boshlanish sanasi')
    tugash_sanasi = models.DateField('Tugash sanasi')
    faol = models.BooleanField('Faol', default=False)
    tavsif = models.TextField('Tavsif', blank=True)
    yaratilgan_sana = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Qabul davri'
        verbose_name_plural = 'Qabul davrlari'
        ordering = ['-yil']

    def __str__(self):
        return f"{self.nomi} - {self.yil}"
