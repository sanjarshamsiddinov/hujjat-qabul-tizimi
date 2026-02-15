"""
O'zbekiston Respublikasi barcha oliy ta'lim muassasalarini yuklash
python manage.py load_universities
"""
from django.core.management.base import BaseCommand
from core.models import University


class Command(BaseCommand):
    help = "O'zbekiston OTMlarini bazaga yuklash (DTM ro'yxati asosida)"

    def handle(self, *args, **options):
        self.stdout.write("O'zbekiston OTMlari yuklanmoqda...\n")

        universities_data = [
            # ============================================================
            # I. DAVLAT OLIY TA'LIM MUASSASALARI
            # ============================================================

            # --- Toshkent shahri ---
            {'nomi': "Mirzo Ulug'bek nomidagi O'zbekiston Milliy universiteti", 'kodi': 'OzMU', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Islom Karimov nomidagi Toshkent davlat texnika universiteti", 'kodi': 'TDTU', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Muhammad al-Xorazmiy nomidagi Toshkent axborot texnologiyalari universiteti", 'kodi': 'TATU', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Toshkent davlat iqtisodiyot universiteti", 'kodi': 'TDIU', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Toshkent davlat yuridik universiteti", 'kodi': 'TDYU', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Nizomiy nomidagi Toshkent davlat pedagogika universiteti", 'kodi': 'TDPU', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Toshkent davlat sharqshunoslik universiteti", 'kodi': 'TDSHI', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Toshkent davlat transport universiteti", 'kodi': 'TDTrU', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Toshkent davlat agrar universiteti", 'kodi': 'TDAU', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Toshkent arxitektura-qurilish universiteti", 'kodi': 'TAQU', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Alisher Navoiy nomidagi Toshkent davlat o'zbek tili va adabiyoti universiteti", 'kodi': 'TDOzTAU', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "O'zbekiston davlat jahon tillari universiteti", 'kodi': 'OzDJTU', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "O'zbekiston jurnalistika va ommaviy kommunikatsiyalar universiteti", 'kodi': 'OzJOKU', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Jahon iqtisodiyoti va diplomatiya universiteti", 'kodi': 'JIDU', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Toshkent moliya instituti", 'kodi': 'TMI', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Toshkent tibbiyot akademiyasi", 'kodi': 'TTA', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Toshkent pediatriya tibbiyot instituti", 'kodi': 'ToshPTI', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Toshkent davlat stomatologiya instituti", 'kodi': 'TDSI', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Toshkent farmatsevtika instituti", 'kodi': 'TFI', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Toshkent kimyo-texnologiya instituti", 'kodi': 'TKTI', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Toshkent to'qimachilik va yengil sanoat instituti", 'kodi': 'TTYSI', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Toshkent irrigatsiya va qishloq xo'jaligini mexanizatsiyalash muhandislari instituti (TIQXMMI)", 'kodi': 'TIQXMMI', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "O'zbekiston davlat jismoniy tarbiya va sport universiteti", 'kodi': 'OzDJTSU', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Geologiya fanlari universiteti", 'kodi': 'GFU', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Jamoat xavfsizligi universiteti", 'kodi': 'JXU', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Kamoliddin Behzod nomidagi Milliy rassomlik va dizayn instituti", 'kodi': 'MRDI', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "O'zbekiston davlat san'at va madaniyat instituti", 'kodi': 'OzDSMI', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "O'zbekiston davlat konservatoriyasi", 'kodi': 'OzDK', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "O'zbek milliy musiqa san'ati instituti", 'kodi': 'OzMMSI', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "O'zbekiston davlat xoreografiya akademiyasi", 'kodi': 'OzDXA', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Milliy estrada san'ati instituti", 'kodi': 'MESI', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Oliy sport mahorati instituti", 'kodi': 'OSMI', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "O'zbekiston xalqaro islomshunoslik akademiyasi", 'kodi': 'OzXIA', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Imom Buxoriy nomidagi Toshkent islom instituti", 'kodi': 'TII', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Mehnat va ijtimoiy munosabatlar akademiyasi", 'kodi': 'MIMA', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "O'zbekiston Respublikasi Huquqni muhofaza qilish akademiyasi", 'kodi': 'HMQA', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Davlat soliq qo'mitasi huzuridagi Fiskal institut", 'kodi': 'FI', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "Oziq-ovqat texnologiyasi va muhandisligi xalqaro instituti", 'kodi': 'OOTMXI', 'turi': 'davlat', 'viloyat': 'Toshkent'},
            {'nomi': "O'zbekiston-Finlyandiya pedagogika instituti", 'kodi': 'OzFPI', 'turi': 'davlat', 'viloyat': 'Toshkent'},

            # --- Toshkent viloyati ---
            {'nomi': "Chirchiq davlat pedagogika universiteti", 'kodi': 'ChDPU', 'turi': 'davlat', 'viloyat': 'Toshkent viloyati'},

            # --- Samarqand viloyati ---
            {'nomi': "Sharof Rashidov nomidagi Samarqand davlat universiteti", 'kodi': 'SamDU', 'turi': 'davlat', 'viloyat': 'Samarqand'},
            {'nomi': "Samarqand davlat tibbiyot universiteti", 'kodi': 'SamDTU', 'turi': 'davlat', 'viloyat': 'Samarqand'},
            {'nomi': "Mirzo Ulug'bek nomidagi Samarqand davlat arxitektura-qurilish universiteti", 'kodi': 'SamDAQU', 'turi': 'davlat', 'viloyat': 'Samarqand'},
            {'nomi': "Samarqand davlat veterinariya meditsinasi, chorvachilik va biotexnologiyalar universiteti", 'kodi': 'SamDVMU', 'turi': 'davlat', 'viloyat': 'Samarqand'},
            {'nomi': "Samarqand davlat chet tillar instituti", 'kodi': 'SamDChTI', 'turi': 'davlat', 'viloyat': 'Samarqand'},
            {'nomi': "Samarqand iqtisodiyot va servis instituti", 'kodi': 'SamISI', 'turi': 'davlat', 'viloyat': 'Samarqand'},
            {'nomi': "\"Ipak yo'li\" turizm va madaniy meros xalqaro universiteti", 'kodi': 'IYU', 'turi': 'davlat', 'viloyat': 'Samarqand'},
            {'nomi': "Shahrisabz davlat pedagogika instituti", 'kodi': 'ShDPI', 'turi': 'davlat', 'viloyat': 'Samarqand'},

            # --- Buxoro viloyati ---
            {'nomi': "Buxoro davlat universiteti", 'kodi': 'BuxDU', 'turi': 'davlat', 'viloyat': 'Buxoro'},
            {'nomi': "Buxoro muhandislik-texnologiya instituti", 'kodi': 'BuxMTI', 'turi': 'davlat', 'viloyat': 'Buxoro'},
            {'nomi': "Abu Ali ibn Sino nomidagi Buxoro davlat tibbiyot instituti", 'kodi': 'BuxDTI', 'turi': 'davlat', 'viloyat': 'Buxoro'},
            {'nomi': "Buxoro davlat pedagogika instituti", 'kodi': 'BuxDPI', 'turi': 'davlat', 'viloyat': 'Buxoro'},
            {'nomi': "Buxoro tabiiy resurslarni boshqarish instituti", 'kodi': 'BuxTRBI', 'turi': 'davlat', 'viloyat': 'Buxoro'},

            # --- Andijon viloyati ---
            {'nomi': "Zahiriddin Muhammad Bobur nomidagi Andijon davlat universiteti", 'kodi': 'AndDU', 'turi': 'davlat', 'viloyat': 'Andijon'},
            {'nomi': "Andijon davlat tibbiyot instituti", 'kodi': 'AndDTI', 'turi': 'davlat', 'viloyat': 'Andijon'},
            {'nomi': "Andijon davlat pedagogika instituti", 'kodi': 'AndDPI', 'turi': 'davlat', 'viloyat': 'Andijon'},
            {'nomi': "Andijon davlat chet tillari instituti", 'kodi': 'AndDChTI', 'turi': 'davlat', 'viloyat': 'Andijon'},
            {'nomi': "Andijon mashinasozlik instituti", 'kodi': 'AndMI', 'turi': 'davlat', 'viloyat': 'Andijon'},
            {'nomi': "Andijon qishloq xo'jaligi va agrotexnologiyalar instituti", 'kodi': 'AndQXAI', 'turi': 'davlat', 'viloyat': 'Andijon'},
            {'nomi': "Andijon iqtisodiyot va qurilish instituti", 'kodi': 'AndIQI', 'turi': 'davlat', 'viloyat': 'Andijon'},

            # --- Farg'ona viloyati ---
            {'nomi': "Farg'ona davlat universiteti", 'kodi': 'FarDU', 'turi': 'davlat', 'viloyat': "Farg'ona"},
            {'nomi': "Farg'ona politexnika instituti", 'kodi': 'FarPI', 'turi': 'davlat', 'viloyat': "Farg'ona"},
            {'nomi': "Farg'ona jamoat salomatligi tibbiyot instituti", 'kodi': 'FarJSTI', 'turi': 'davlat', 'viloyat': "Farg'ona"},
            {'nomi': "Qo'qon davlat pedagogika instituti", 'kodi': 'QoqDPI', 'turi': 'davlat', 'viloyat': "Farg'ona"},

            # --- Namangan viloyati ---
            {'nomi': "Namangan davlat universiteti", 'kodi': 'NamDU', 'turi': 'davlat', 'viloyat': 'Namangan'},
            {'nomi': "Namangan davlat pedagogika instituti", 'kodi': 'NamDPI', 'turi': 'davlat', 'viloyat': 'Namangan'},
            {'nomi': "Namangan davlat chet tillari instituti", 'kodi': 'NamDChTI', 'turi': 'davlat', 'viloyat': 'Namangan'},
            {'nomi': "Namangan muhandislik-qurilish instituti", 'kodi': 'NamMQI', 'turi': 'davlat', 'viloyat': 'Namangan'},
            {'nomi': "Namangan muhandislik-texnologiya instituti", 'kodi': 'NamMTI', 'turi': 'davlat', 'viloyat': 'Namangan'},
            {'nomi': "Namangan to'qimachilik sanoati instituti", 'kodi': 'NamTSI', 'turi': 'davlat', 'viloyat': 'Namangan'},

            # --- Xorazm viloyati ---
            {'nomi': "Abu Rayhon Beruniy nomidagi Urganch davlat universiteti", 'kodi': 'UrDU', 'turi': 'davlat', 'viloyat': 'Xorazm'},
            {'nomi': "Urganch davlat pedagogika instituti", 'kodi': 'UrDPI', 'turi': 'davlat', 'viloyat': 'Xorazm'},

            # --- Qashqadaryo viloyati ---
            {'nomi': "Qarshi davlat universiteti", 'kodi': 'QarDU', 'turi': 'davlat', 'viloyat': 'Qashqadaryo'},
            {'nomi': "Qarshi muhandislik-iqtisodiyot instituti", 'kodi': 'QarMII', 'turi': 'davlat', 'viloyat': 'Qashqadaryo'},
            {'nomi': "Qarshi irrigatsiya va agrotexnologiyalar instituti", 'kodi': 'QarIAI', 'turi': 'davlat', 'viloyat': 'Qashqadaryo'},

            # --- Surxondaryo viloyati ---
            {'nomi': "Termiz davlat universiteti", 'kodi': 'TerDU', 'turi': 'davlat', 'viloyat': 'Surxondaryo'},
            {'nomi': "Termiz davlat pedagogika instituti", 'kodi': 'TerDPI', 'turi': 'davlat', 'viloyat': 'Surxondaryo'},
            {'nomi': "Termiz agrotexnologiyalar va innovatsion rivojlanish instituti", 'kodi': 'TerAIRI', 'turi': 'davlat', 'viloyat': 'Surxondaryo'},
            {'nomi': "Denov tadbirkorlik va pedagogika instituti", 'kodi': 'DenTPI', 'turi': 'davlat', 'viloyat': 'Surxondaryo'},

            # --- Sirdaryo viloyati ---
            {'nomi': "Guliston davlat universiteti", 'kodi': 'GulDU', 'turi': 'davlat', 'viloyat': 'Sirdaryo'},
            {'nomi': "Guliston davlat pedagogika instituti", 'kodi': 'GulDPI', 'turi': 'davlat', 'viloyat': 'Sirdaryo'},

            # --- Navoiy viloyati ---
            {'nomi': "Navoiy davlat konchilik va texnologiyalar universiteti", 'kodi': 'NavDKTU', 'turi': 'davlat', 'viloyat': 'Navoiy'},
            {'nomi': "Navoiy davlat pedagogika instituti", 'kodi': 'NavDPI', 'turi': 'davlat', 'viloyat': 'Navoiy'},

            # --- Jizzax viloyati ---
            {'nomi': "Jizzax davlat pedagogika universiteti", 'kodi': 'JizDPU', 'turi': 'davlat', 'viloyat': 'Jizzax'},

            # --- Qoraqalpog'iston Respublikasi ---
            {'nomi': "Berdaq nomidagi Qoraqalpoq davlat universiteti", 'kodi': 'QarDU_N', 'turi': 'davlat', 'viloyat': "Qoraqalpog'iston"},
            {'nomi': "Ajiniyoz nomidagi Nukus davlat pedagogika instituti", 'kodi': 'NukDPI', 'turi': 'davlat', 'viloyat': "Qoraqalpog'iston"},
            {'nomi': "Qoraqalpog'iston tibbiyot instituti", 'kodi': 'QarTI', 'turi': 'davlat', 'viloyat': "Qoraqalpog'iston"},
            {'nomi': "Qoraqalpog'iston qishloq xo'jaligi va agrotexnologiyalar instituti", 'kodi': 'QarQXAI', 'turi': 'davlat', 'viloyat': "Qoraqalpog'iston"},

            # --- Davlat universitetlar filiallari ---
            {'nomi': "O'zbekiston Milliy universitetining Jizzax filiali", 'kodi': 'OzMU_Jiz', 'turi': 'davlat', 'viloyat': 'Jizzax'},
            {'nomi': "Toshkent davlat texnika universitetining Olmaliq filiali", 'kodi': 'TDTU_Olm', 'turi': 'davlat', 'viloyat': 'Toshkent viloyati'},
            {'nomi': "Toshkent davlat texnika universitetining Termiz filiali", 'kodi': 'TDTU_Ter', 'turi': 'davlat', 'viloyat': 'Surxondaryo'},
            {'nomi': "TATU Farg'ona filiali", 'kodi': 'TATU_Far', 'turi': 'davlat', 'viloyat': "Farg'ona"},
            {'nomi': "TATU Qarshi filiali", 'kodi': 'TATU_Qar', 'turi': 'davlat', 'viloyat': 'Qashqadaryo'},
            {'nomi': "TATU Samarqand filiali", 'kodi': 'TATU_Sam', 'turi': 'davlat', 'viloyat': 'Samarqand'},
            {'nomi': "TATU Urganch filiali", 'kodi': 'TATU_Urg', 'turi': 'davlat', 'viloyat': 'Xorazm'},
            {'nomi': "TATU Nukus filiali", 'kodi': 'TATU_Nuk', 'turi': 'davlat', 'viloyat': "Qoraqalpog'iston"},
            {'nomi': "TATU Nurafshon filiali", 'kodi': 'TATU_Nur', 'turi': 'davlat', 'viloyat': 'Toshkent viloyati'},
            {'nomi': "Toshkent tibbiyot akademiyasi Urganch filiali", 'kodi': 'TTA_Urg', 'turi': 'davlat', 'viloyat': 'Xorazm'},
            {'nomi': "Toshkent tibbiyot akademiyasi Termiz filiali", 'kodi': 'TTA_Ter', 'turi': 'davlat', 'viloyat': 'Surxondaryo'},
            {'nomi': "Toshkent kimyo-texnologiya instituti Shahrisabz filiali", 'kodi': 'TKTI_Sha', 'turi': 'davlat', 'viloyat': 'Qashqadaryo'},

            # ============================================================
            # II. XORIJIY UNIVERSITETLAR FILIALLARI
            # ============================================================
            {'nomi': "Toshkentdagi Xalqaro Westminster universiteti (WIUT)", 'kodi': 'WIUT', 'turi': 'xorijiy', 'viloyat': 'Toshkent'},
            {'nomi': "Toshkent shahridagi Turin politexnika universiteti", 'kodi': 'TTPU', 'turi': 'xorijiy', 'viloyat': 'Toshkent'},
            {'nomi': "Toshkent shahridagi Inha universiteti (IUT)", 'kodi': 'IUT', 'turi': 'xorijiy', 'viloyat': 'Toshkent'},
            {'nomi': "M.V. Lomonosov nomidagi MDU Toshkent filiali", 'kodi': 'MDU_Tosh', 'turi': 'xorijiy', 'viloyat': 'Toshkent'},
            {'nomi': "G.V. Plexanov nomidagi Rossiya iqtisodiyot universiteti Toshkent filiali", 'kodi': 'REU_Tosh', 'turi': 'xorijiy', 'viloyat': 'Toshkent'},
            {'nomi': "I.M. Gubkin nomidagi Rossiya neft va gaz universiteti Toshkent filiali", 'kodi': 'Gubkin_Tosh', 'turi': 'xorijiy', 'viloyat': 'Toshkent'},
            {'nomi': "MGIMO Toshkent filiali", 'kodi': 'MGIMO_Tosh', 'turi': 'xorijiy', 'viloyat': 'Toshkent'},
            {'nomi': "D.I. Mendeleev nomidagi Rossiya kimyo-texnologiya universiteti Toshkent filiali", 'kodi': 'RXTU_Tosh', 'turi': 'xorijiy', 'viloyat': 'Toshkent'},
            {'nomi': "Toshkent shahridagi Yeoju texnika instituti", 'kodi': 'Yeoju', 'turi': 'xorijiy', 'viloyat': 'Toshkent'},
            {'nomi': "Toshkent shahridagi Puchon universiteti", 'kodi': 'Bucheon', 'turi': 'xorijiy', 'viloyat': 'Toshkent'},
            {'nomi': "Toshkent shahridagi Amity universiteti", 'kodi': 'Amity', 'turi': 'xorijiy', 'viloyat': 'Toshkent'},
            {'nomi': "Toshkentdagi Singapur menejmentni rivojlantirish instituti (MDIS)", 'kodi': 'MDIS', 'turi': 'xorijiy', 'viloyat': 'Toshkent'},
            {'nomi': "Toshkent shahridagi Vebster universiteti", 'kodi': 'Webster', 'turi': 'xorijiy', 'viloyat': 'Toshkent'},
            {'nomi': "Turkiya iqtisodiyot va texnologiyalar universiteti Toshkent filiali", 'kodi': 'TETU_Tosh', 'turi': 'xorijiy', 'viloyat': 'Toshkent'},
            {'nomi': "Toshkent shahridagi Ajou (ADJU) universiteti", 'kodi': 'ADJU', 'turi': 'xorijiy', 'viloyat': 'Toshkent'},
            {'nomi': "Farg'ona shahridagi Koreya xalqaro universiteti", 'kodi': 'KIU_Far', 'turi': 'xorijiy', 'viloyat': "Farg'ona"},
            {'nomi': "Sharda universiteti (Andijon)", 'kodi': 'Sharda', 'turi': 'xorijiy', 'viloyat': 'Andijon'},
            {'nomi': "MEPI Milliy yadro tadqiqot universiteti Toshkent filiali", 'kodi': 'MEPI_Tosh', 'turi': 'xorijiy', 'viloyat': 'Toshkent'},

            # ============================================================
            # III. NODAVLAT (XUSUSIY) OLIY TA'LIM MUASSASALARI
            # ============================================================
            {'nomi': "Akfa universiteti", 'kodi': 'AKFA', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Alfraganus University", 'kodi': 'ALFR', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Binary International University", 'kodi': 'BINARY', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Britaniya menejment universiteti", 'kodi': 'BMU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Buxoro innovatsion tibbiyot instituti", 'kodi': 'BuxITI', 'turi': 'xususiy', 'viloyat': 'Buxoro'},
            {'nomi': "Buxoro innovatsiyalar universiteti", 'kodi': 'BuxIU', 'turi': 'xususiy', 'viloyat': 'Buxoro'},
            {'nomi': "Cambridge International University", 'kodi': 'CamIU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Capital School - Innovatsion va ijtimoiy-iqtisodiyot universiteti", 'kodi': 'CapSch', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Central Asian Medical University", 'kodi': 'CAMU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Digital University", 'kodi': 'DigU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Diplomat University", 'kodi': 'DipU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "European Medical University", 'kodi': 'EMU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Fan va texnologiyalar universiteti", 'kodi': 'FTU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Impuls tibbiyot instituti", 'kodi': 'ImpTI', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "International School of Finance and Technology", 'kodi': 'ISFT', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Iqtisodiyot va pedagogika universiteti", 'kodi': 'IPU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "IT-Park University", 'kodi': 'ITPU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Japan Digital University", 'kodi': 'JDU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Kokand University", 'kodi': 'KokU', 'turi': 'xususiy', 'viloyat': "Farg'ona"},
            {'nomi': "Ma'mun universiteti", 'kodi': 'MamU', 'turi': 'xususiy', 'viloyat': 'Xorazm'},
            {'nomi': "Millat Umidi University", 'kodi': 'MUU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Navoiy innovatsiyalar instituti", 'kodi': 'NavII', 'turi': 'xususiy', 'viloyat': 'Navoiy'},
            {'nomi': "Nukus innovatsion instituti", 'kodi': 'NukII', 'turi': 'xususiy', 'viloyat': "Qoraqalpog'iston"},
            {'nomi': "Oriental University", 'kodi': 'OrU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Osiyo xalqaro universiteti", 'kodi': 'OXU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Osiyo texnologiyalar universiteti", 'kodi': 'OTxU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Oxus universiteti", 'kodi': 'OxusU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "PDP University", 'kodi': 'PDPU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Perfect University", 'kodi': 'PerfU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Profi University", 'kodi': 'ProfiU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Qarshi innovatsion ta'lim universiteti", 'kodi': 'QarITU', 'turi': 'xususiy', 'viloyat': 'Qashqadaryo'},
            {'nomi': "Qarshi xalqaro universiteti", 'kodi': 'QarXU', 'turi': 'xususiy', 'viloyat': 'Qashqadaryo'},
            {'nomi': "Raqamli iqtisodiyot va agrotexnologiyalar universiteti", 'kodi': 'RIAU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Renessans ta'lim universiteti", 'kodi': 'RenU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Samarqand xalqaro texnologiya universiteti", 'kodi': 'SamXTU', 'turi': 'xususiy', 'viloyat': 'Samarqand'},
            {'nomi': "Sharq universiteti", 'kodi': 'SharqU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "STARS International University", 'kodi': 'STARS', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Tashkent International University of Education", 'kodi': 'TIUE', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "TEAM University", 'kodi': 'TEAM', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Termiz iqtisodiyot va servis universiteti", 'kodi': 'TerISU', 'turi': 'xususiy', 'viloyat': 'Surxondaryo'},
            {'nomi': "Toshkent amaliy fanlar universiteti", 'kodi': 'ToshAFU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Toshkent menejment va iqtisodiyot universiteti", 'kodi': 'ToshMIU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Turan International University", 'kodi': 'TuranU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Turon Zarmed universiteti", 'kodi': 'TZU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "University of Business and Science", 'kodi': 'UBS', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Urganch innovatsion universiteti", 'kodi': 'UrgIU', 'turi': 'xususiy', 'viloyat': 'Xorazm'},
            {'nomi': "Xalqaro innovatsion universiteti", 'kodi': 'XIU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Xalqaro Nordik universiteti", 'kodi': 'XNU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},
            {'nomi': "Yangi asr universiteti", 'kodi': 'YAU', 'turi': 'xususiy', 'viloyat': 'Toshkent'},

            # ============================================================
            # IV. HARBIY OLIY TA'LIM MUASSASALARI
            # ============================================================
            {'nomi': "O'zbekiston Respublikasi Qurolli Kuchlar akademiyasi", 'kodi': 'QKA', 'turi': 'harbiy', 'viloyat': 'Toshkent'},
            {'nomi': "Chirchiq oliy tank qo'mondonlik-muhandislik bilim yurti", 'kodi': 'ChOTQMBY', 'turi': 'harbiy', 'viloyat': 'Toshkent viloyati'},
            {'nomi': "Samarqand oliy harbiy avtomobil qo'mondonlik-muhandislik bilim yurti", 'kodi': 'SamOHABY', 'turi': 'harbiy', 'viloyat': 'Samarqand'},
            {'nomi': "Jizzax oliy harbiy aviatsiya bilim yurti", 'kodi': 'JizOHABY', 'turi': 'harbiy', 'viloyat': 'Jizzax'},
            {'nomi': "O'zbekiston Respublikasi IIV Akademiyasi", 'kodi': 'IIVA', 'turi': 'harbiy', 'viloyat': 'Toshkent'},
            {'nomi': "Mudofaa vazirligi axborot-kommunikatsiya texnologiyalari va aloqa harbiy instituti", 'kodi': 'MV_AKTAHI', 'turi': 'harbiy', 'viloyat': 'Toshkent'},
            {'nomi': "Davlat xavfsizlik xizmati akademiyasi", 'kodi': 'DXXA', 'turi': 'harbiy', 'viloyat': 'Toshkent'},
            {'nomi': "Favqulodda vaziyatlar vazirligi akademiyasi", 'kodi': 'FVVA', 'turi': 'harbiy', 'viloyat': 'Toshkent'},
        ]

        created_count = 0
        existing_count = 0

        for data in universities_data:
            uni, created = University.objects.get_or_create(
                kodi=data['kodi'],
                defaults=data
            )
            if created:
                created_count += 1
                self.stdout.write(f"  + {uni.nomi}")
            else:
                existing_count += 1

        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS(f"Jami: {created_count} ta yangi OTM yaratildi, {existing_count} ta mavjud edi."))

        # Stats
        from django.db.models import Count
        type_stats = University.objects.values('turi').annotate(soni=Count('id')).order_by('turi')
        for stat in type_stats:
            label = dict(University.UNIVERSITY_TYPES).get(stat['turi'], stat['turi'])
            self.stdout.write(f"  {label}: {stat['soni']} ta")

        self.stdout.write(self.style.SUCCESS(f"\nBarcha OTMlar soni: {University.objects.count()}"))
