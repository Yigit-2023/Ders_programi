#Yapımcı:
#Yiğit Çıtak
Version = "1.0"
ders_list = """
Ders/gün	 1	  2	  3	  4	  5	  6	  7	  8
------------------------------------------------------------------------------------------
Saat|	       08:40 	09:40	10:30	11:20	12:10	13:40	14:30	15:20
------------------------------------------------------------------------------------------		
Pazartesi|	M.ARP	M.ARP	DM3	ADAP	KLM3	KLM3	TDE32	SÇTDT			
Salı	 |      SCOĞ1	SCOĞ1	KURAN	KURAN	M.ARP	BEDEN1	TDE32	TDE32				
Çarşamba |	S TED	S TED 	İNK3	İNK3	İNG4	İNG4	TDE32	TDE32				
Perşembe |	SCOĞ1	SCOĞ1	İKMT2	İKMT2	KDT	KDT	KURAN	SÇTDT				
Saat	 |      08:40	09:30	10:20	11:10	12:00	13:50	14:40	15:30				
Cuma	 |      SMAN4	SMAN4	STMAT1	STMAT1	SÇTDT	SÇTDT	SFIKO	SFIKO				
-------------------------------------------------------------------------------------------												
												
											|17.09.2023|	
																	
"""
#Kopyala Yapıştır:	1- 2- 3- 4- 5- 6- 7- 8-
pazartesi = """\n1-M.Arapça 2-M.Arapça 3-Dini Müsiki 4-Adabı Muaşeret 5-Kalem 6-Kalem 7-Türk Dili edebiyat 8-Seçmeli Türk Dili Edebiyat"""
sali = """\n1-Seçmeli Coğrafya 2-Seçmeli Coğrafya 3-Kuran 4-Kuran 5-Arapça 6-Beden 7-Türk Dili edebiyat 8-Türk Dili edebiyat"""
carsamba = """\n1-Seçmeli Edebiyat 2-Seçmeli Edebiyat 3-İnkılap 4-İnkılap 5-İngilizce 6-İngilizce 7-Türk Dili edebiyat 8-Türk Dili edebiyat"""
persembe = """\n1-Seçmeli Coğrafya 2-Seçmeli Coğrafya 3-İslam kültür ve medeniyeti 4-İslam kültür ve medeniyeti \n5-Dinler Tarihi	6-Dinler Tarihi	7-Kuran	8-Seçmeli Türk Dili Edebiyat"""
cuma = """\n1-Seçmeli Mantık 2-Seçmeli Mantık 3-S.Temel Matematik 4-S.Temel Matematik 5-Seçmeli Türk Dili Edebiyat 6-Seçmeli Türk Dili Edebiyat 7-Seçmeli Fıkıh 8-Seçmeli Fıkıh"""

print("12-B Sınıfı Ders Programı\nSürüm:\t",Version,"\n")

print(ders_list)

dongu_of_or_on = True

while dongu_of_or_on:

	ilk_girdi = input("\nHangi Günü incelemek istiyorsun?\n\n")

	if ilk_girdi == "pazartesi" or ilk_girdi == "PAZARTESİ":
		print(pazartesi)
		

	elif ilk_girdi == "salı" or ilk_girdi == "SALI":
		print(sali)
		

	elif ilk_girdi == "çarşamba" or ilk_girdi == "ÇARŞAMBA":
		print(carsamba)
		

	elif ilk_girdi == "perşembe" or ilk_girdi == "PERŞEMBE":
		print(persembe)
		
	elif ilk_girdi == "cuma" or ilk_girdi == "CUMA":
		print(cuma)

	elif ilk_girdi == "Yapımcı":
		print("\nYiğit Çıtak\n")

	elif ilk_girdi == "Kaynak kod":
		print("https://github.com/Yigit-2023/Ders_programi")
		
	else:
		print("\nLütfen Gün adı girin\n")
