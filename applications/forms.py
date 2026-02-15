import os
from django import forms
from .models import Application, Document
from core.models import Specialty, AdmissionCampaign


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['yonalish']
        widgets = {
            'yonalish': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['yonalish'].queryset = Specialty.objects.filter(faol=True)
        self.fields['yonalish'].label = "Yo'nalishni tanlang"


class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['hujjat_turi', 'fayl']
        widgets = {
            'hujjat_turi': forms.Select(attrs={'class': 'form-select'}),
            'fayl': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf,.jpg,.jpeg,.png'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hujjat_turi'].label = "Hujjat turini tanlang"
        self.fields['fayl'].label = "Faylni tanlang"

    def clean_fayl(self):
        fayl = self.cleaned_data.get('fayl')
        if fayl:
            # Check file size (5MB limit)
            if fayl.size > 5 * 1024 * 1024:
                raise forms.ValidationError(
                    "Fayl hajmi 5MB dan oshmasligi kerak. "
                    f"Joriy hajm: {fayl.size / (1024 * 1024):.1f}MB"
                )
            # Check file extension
            ext = os.path.splitext(fayl.name)[1].lower()
            allowed = ['.pdf', '.jpg', '.jpeg', '.png']
            if ext not in allowed:
                raise forms.ValidationError(
                    f"Faqat {', '.join(allowed)} formatlariga ruxsat berilgan. "
                    f"Yuklangan format: {ext}"
                )
            # Check content type
            allowed_types = [
                'application/pdf',
                'image/jpeg',
                'image/png',
            ]
            if hasattr(fayl, 'content_type') and fayl.content_type not in allowed_types:
                raise forms.ValidationError("Fayl formati noto'g'ri.")
        return fayl


class DocumentReviewForm(forms.Form):
    HOLAT_CHOICES = [
        ('tasdiqlangan', 'Tasdiqlash'),
        ('rad_etildi', 'Rad etish'),
    ]
    holat = forms.ChoiceField(
        choices=HOLAT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Holat',
    )
    izoh = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Izoh qoldiring...',
        }),
        required=False,
        label='Izoh',
    )


class ApplicationStatusForm(forms.Form):
    STATUS_CHOICES = [
        ('yangi', 'Yangi'),
        ('korib_chiqilmoqda', "Ko'rib chiqilmoqda"),
        ('qabul_qilindi', 'Qabul qilindi'),
        ('rad_etildi', 'Rad etildi'),
    ]
    holat = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Holat',
    )
    izoh = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Izoh qoldiring...',
        }),
        required=False,
        label='Izoh',
    )
