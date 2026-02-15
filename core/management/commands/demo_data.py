"""
Demo ma'lumotlarni yaratish buyrug'i
python manage.py demo_data
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import ApplicantProfile, StaffProfile
from core.models import Faculty, Specialty, AdmissionCampaign
from applications.models import DocumentType, Application
from datetime import date


class Command(BaseCommand):
    help = "Demo ma'lumotlarni yaratish"

    def handle(self, *args, **options):
        self.stdout.write("Demo ma'lumotlar yaratilmoqda...")

        # 1. Fakultetlar
        faculties_data = [
            {'nomi': 'Axborot texnologiyalari fakulteti', 'kodi': 'ATF', 'tavsif': 'Kompyuter fanlari, dasturlash va axborot texnologiyalari yo\'nalishlarini o\'z ichiga oladi.'},
            {'nomi': 'Iqtisodiyot fakulteti', 'kodi': 'IQF', 'tavsif': 'Iqtisodiyot, moliya, buxgalteriya va menejment yo\'nalishlarini o\'z ichiga oladi.'},
            {'nomi': 'Filologiya fakulteti', 'kodi': 'FF', 'tavsif': 'O\'zbek tili, ingliz tili, rus tili va adabiyot yo\'nalishlarini o\'z ichiga oladi.'},
            {'nomi': 'Tabiiy fanlar fakulteti', 'kodi': 'TFF', 'tavsif': 'Matematika, fizika, kimyo va biologiya yo\'nalishlarini o\'z ichiga oladi.'},
            {'nomi': 'Huquqshunoslik fakulteti', 'kodi': 'HF', 'tavsif': 'Huquqshunoslik, xalqaro huquq va davlat boshqaruvi yo\'nalishlarini o\'z ichiga oladi.'},
        ]
        faculties = []
        for data in faculties_data:
            f, created = Faculty.objects.get_or_create(kodi=data['kodi'], defaults=data)
            faculties.append(f)
            if created:
                self.stdout.write(f"  + Fakultet: {f.nomi}")

        # 2. Yo'nalishlar
        specialties_data = [
            # ATF
            {'nomi': 'Kompyuter injiniringi', 'kodi': '60610', 'fakultet': faculties[0], 'talim_turi': 'bakalavr', 'kvota': 50},
            {'nomi': 'Dasturiy injiniring', 'kodi': '60611', 'fakultet': faculties[0], 'talim_turi': 'bakalavr', 'kvota': 45},
            {'nomi': 'Axborot xavfsizligi', 'kodi': '60612', 'fakultet': faculties[0], 'talim_turi': 'bakalavr', 'kvota': 30},
            {'nomi': 'Sun\'iy intellekt', 'kodi': '70610', 'fakultet': faculties[0], 'talim_turi': 'magistr', 'kvota': 15},
            # IQF
            {'nomi': 'Iqtisodiyot', 'kodi': '60310', 'fakultet': faculties[1], 'talim_turi': 'bakalavr', 'kvota': 40},
            {'nomi': 'Moliya va moliyaviy texnologiyalar', 'kodi': '60311', 'fakultet': faculties[1], 'talim_turi': 'bakalavr', 'kvota': 35},
            {'nomi': 'Menejment', 'kodi': '60312', 'fakultet': faculties[1], 'talim_turi': 'bakalavr', 'kvota': 30},
            # FF
            {'nomi': 'Ingliz tili va adabiyoti', 'kodi': '60220', 'fakultet': faculties[2], 'talim_turi': 'bakalavr', 'kvota': 40},
            {'nomi': "O'zbek filologiyasi", 'kodi': '60221', 'fakultet': faculties[2], 'talim_turi': 'bakalavr', 'kvota': 35},
            # TFF
            {'nomi': 'Amaliy matematika', 'kodi': '60110', 'fakultet': faculties[3], 'talim_turi': 'bakalavr', 'kvota': 30},
            {'nomi': 'Fizika', 'kodi': '60111', 'fakultet': faculties[3], 'talim_turi': 'bakalavr', 'kvota': 25},
            # HF
            {'nomi': 'Huquqshunoslik', 'kodi': '60410', 'fakultet': faculties[4], 'talim_turi': 'bakalavr', 'kvota': 50},
            {'nomi': 'Xalqaro huquq', 'kodi': '70410', 'fakultet': faculties[4], 'talim_turi': 'magistr', 'kvota': 15},
        ]
        for data in specialties_data:
            s, created = Specialty.objects.get_or_create(kodi=data['kodi'], defaults=data)
            if created:
                self.stdout.write(f"  + Yo'nalish: {s.nomi}")

        # 3. Qabul davri
        campaign, created = AdmissionCampaign.objects.get_or_create(
            yil=2026,
            defaults={
                'nomi': '2026-2027 o\'quv yili uchun qabul',
                'boshlanish_sanasi': date(2026, 6, 1),
                'tugash_sanasi': date(2026, 9, 1),
                'faol': True,
                'tavsif': '2026-2027 o\'quv yili uchun bakalavr va magistratura bosqichlariga qabul.'
            }
        )
        if created:
            self.stdout.write(f"  + Qabul davri: {campaign.nomi}")

        # 4. Hujjat turlari
        doc_types_data = [
            {'nomi': 'Pasport nusxasi', 'majburiy': True, 'tartib': 1, 'tavsif': 'Pasportning asosiy sahifasi va ro\'yxatga olish sahifasining nusxasi'},
            {'nomi': 'Attestat / Diplom nusxasi', 'majburiy': True, 'tartib': 2, 'tavsif': 'O\'rta ta\'lim attestati yoki oliy ta\'lim diplomi nusxasi'},
            {'nomi': '3x4 rasm (6 dona)', 'majburiy': True, 'tartib': 3, 'tavsif': '3x4 sm o\'lchamda 6 dona rangli rasm'},
            {'nomi': 'Tibbiy ma\'lumotnoma (086-shakl)', 'majburiy': True, 'tartib': 4, 'tavsif': 'Sog\'liq haqida tibbiy ma\'lumotnoma'},
            {'nomi': 'Harbiy hisob varaqasi', 'majburiy': False, 'tartib': 5, 'tavsif': 'O\'g\'il bolalar uchun harbiy hisob varaqasi yoki harbiy guvohnoma'},
            {'nomi': 'Imtiyoz beruvchi hujjat', 'majburiy': False, 'tartib': 6, 'tavsif': 'Imtiyoz uchun asos bo\'luvchi hujjat (yetim, nogironlik va h.k.)'},
        ]
        for data in doc_types_data:
            dt, created = DocumentType.objects.get_or_create(nomi=data['nomi'], defaults=data)
            if created:
                self.stdout.write(f"  + Hujjat turi: {dt.nomi}")

        # 5. Admin/Xodim foydalanuvchi
        if not User.objects.filter(username='admin').exists():
            admin_user = User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123',
                first_name='Admin',
                last_name='Tizim'
            )
            StaffProfile.objects.create(
                user=admin_user,
                lavozim='Tizim administratori',
                role='admin',
                telefon='+998 90 123 45 67'
            )
            self.stdout.write("  + Admin yaratildi: admin / admin123")

        # 6. Xodim (reviewer)
        if not User.objects.filter(username='xodim').exists():
            staff_user = User.objects.create_user(
                username='xodim',
                email='xodim@example.com',
                password='xodim123',
                first_name='Aziz',
                last_name='Karimov'
            )
            StaffProfile.objects.create(
                user=staff_user,
                lavozim='Qabul komissiyasi a\'zosi',
                role='reviewer',
                telefon='+998 91 234 56 78'
            )
            self.stdout.write("  + Xodim yaratildi: xodim / xodim123")

        # 7. Test abituriyentlar
        test_applicants = [
            {'username': 'abituriyent1', 'first_name': 'Jasur', 'last_name': 'Toshmatov', 'passport': 'AB 1234567', 'telefon': '+998 93 111 22 33'},
            {'username': 'abituriyent2', 'first_name': 'Dilnoza', 'last_name': 'Rahimova', 'passport': 'AC 7654321', 'telefon': '+998 94 222 33 44'},
            {'username': 'abituriyent3', 'first_name': 'Sardor', 'last_name': 'Aliyev', 'passport': 'AD 9876543', 'telefon': '+998 95 333 44 55'},
        ]
        specialties = list(Specialty.objects.filter(talim_turi='bakalavr')[:3])
        statuses = ['yangi', 'korib_chiqilmoqda', 'qabul_qilindi']

        for i, data in enumerate(test_applicants):
            if not User.objects.filter(username=data['username']).exists():
                user = User.objects.create_user(
                    username=data['username'],
                    password='test1234',
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    email=f"{data['username']}@example.com"
                )
                ApplicantProfile.objects.create(
                    user=user,
                    passport_seriya=data['passport'],
                    telefon=data['telefon'],
                    manzil='Toshkent shahri',
                    tugilgan_sana=date(2005, 1 + i, 15)
                )
                # Create application
                if specialties:
                    Application.objects.create(
                        abituriyent=user,
                        yonalish=specialties[i % len(specialties)],
                        qabul_davri=campaign,
                        holat=statuses[i % len(statuses)]
                    )
                self.stdout.write(f"  + Abituriyent: {data['username']} / test1234")

        self.stdout.write(self.style.SUCCESS("\nDemo ma'lumotlar muvaffaqiyatli yaratildi!"))
        self.stdout.write(self.style.SUCCESS("Admin kirish: admin / admin123"))
        self.stdout.write(self.style.SUCCESS("Xodim kirish: xodim / xodim123"))
        self.stdout.write(self.style.SUCCESS("Abituriyent kirish: abituriyent1 / test1234"))
