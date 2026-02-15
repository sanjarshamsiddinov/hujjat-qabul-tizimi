from django.db import models
from django.contrib.auth.models import User
from core.models import Specialty, AdmissionCampaign

class DocumentType(models.Model):
    nomi = models.CharField('Hujjat turi nomi', max_length=200)
    tavsif = models.TextField('Tavsif', blank=True)
    majburiy = models.BooleanField('Majburiy', default=True)
    tartib = models.PositiveIntegerField('Tartib raqami', default=0)

    class Meta:
        verbose_name = 'Hujjat turi'
        verbose_name_plural = 'Hujjat turlari'
        ordering = ['tartib']

    def __str__(self):
        return self.nomi


class Application(models.Model):
    STATUS_CHOICES = [
        ('yangi', 'Yangi'),
        ('korib_chiqilmoqda', "Ko'rib chiqilmoqda"),
        ('qabul_qilindi', 'Qabul qilindi'),
        ('rad_etildi', 'Rad etildi'),
    ]
    abituriyent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='arizalar', verbose_name='Abituriyent')
    yonalish = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='arizalar', verbose_name="Yo'nalish")
    qabul_davri = models.ForeignKey(AdmissionCampaign, on_delete=models.CASCADE, related_name='arizalar', verbose_name='Qabul davri')
    holat = models.CharField('Holat', max_length=20, choices=STATUS_CHOICES, default='yangi')
    izoh = models.TextField('Izoh', blank=True)
    yaratilgan_sana = models.DateTimeField('Yaratilgan sana', auto_now_add=True)
    yangilangan_sana = models.DateTimeField("Yangilangan sana", auto_now=True)

    class Meta:
        verbose_name = 'Ariza'
        verbose_name_plural = 'Arizalar'
        ordering = ['-yaratilgan_sana']

    def __str__(self):
        return f"Ariza #{self.pk} - {self.abituriyent.get_full_name()} - {self.yonalish}"

    @property
    def holat_rangi(self):
        ranglar = {
            'yangi': 'primary',
            'korib_chiqilmoqda': 'warning',
            'qabul_qilindi': 'success',
            'rad_etildi': 'danger',
        }
        return ranglar.get(self.holat, 'secondary')
    
    @property
    def hujjatlar_soni(self):
        return self.hujjatlar.count()
    
    @property
    def tasdiqlangan_hujjatlar_soni(self):
        return self.hujjatlar.filter(holat='tasdiqlangan').count()


class Document(models.Model):
    STATUS_CHOICES = [
        ('yuklangan', 'Yuklangan'),
        ('tekshirilmoqda', 'Tekshirilmoqda'),
        ('tasdiqlangan', 'Tasdiqlangan'),
        ('rad_etildi', 'Rad etildi'),
    ]
    ariza = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='hujjatlar', verbose_name='Ariza')
    hujjat_turi = models.ForeignKey(DocumentType, on_delete=models.CASCADE, verbose_name='Hujjat turi')
    fayl = models.FileField('Fayl', upload_to='documents/%Y/%m/')
    holat = models.CharField('Holat', max_length=20, choices=STATUS_CHOICES, default='yuklangan')
    izoh = models.TextField('Izoh (xodim uchun)', blank=True)
    yuklangan_sana = models.DateTimeField('Yuklangan sana', auto_now_add=True)
    tekshirgan = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tekshirgan_hujjatlar', verbose_name='Tekshirgan xodim')

    class Meta:
        verbose_name = 'Hujjat'
        verbose_name_plural = 'Hujjatlar'
        ordering = ['hujjat_turi__tartib']

    def __str__(self):
        return f"{self.hujjat_turi.nomi} - {self.ariza}"

    @property
    def holat_rangi(self):
        ranglar = {
            'yuklangan': 'info',
            'tekshirilmoqda': 'warning',
            'tasdiqlangan': 'success',
            'rad_etildi': 'danger',
        }
        return ranglar.get(self.holat, 'secondary')
