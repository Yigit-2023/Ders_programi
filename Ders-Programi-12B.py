#Yapımcı:
#Yiğit Çıtak
Version = "1.1"
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
adap = "Adabı Muaşeret "
beden1 = "Beden "
dm3 = "Dini Müsiki "
ikmt2 = "İslam Kültür ve medeniyeti "
ing4 = "İngilizce "
ink3 = "T.C inkılap "
kdt = "Dinler Tarihi "
klm3 = "Kalem "
kur = "Kuran "
m_arp = "arapça "
s_ted = "Seçmeli Türk ve dünya tarihi "
s_cog = "Seçmeli coğrafya "
sctdt = "Çağdaş türk ve dünya tarihi "
sfiko = "Seçmeli fıkıh "
man = "Mantık "
mat = "Matematik "
tde32 = "Türk Dili ve edebiyatı "

#Ders saatleri
ders1 = "08:40 - 09:20"
ders2 = "09:40 - 10:20"
ders3 = "10:30 - 11:10"
ders4 = "11:20 - 12:00"
ders5 = "12:10 - 12:50"
ders6 = "13:40 - 14:20"
ders7 = "14:30 - 15:10"
ders8 = "15:20 - 16:00"

#cuma günü

c_ders1 = "08:40 - 09:20"
c_ders2 = "09:30 - 10:10"
c_ders3 = "10:20 - 11:00"
c_ders4 = "11:10 - 11:50"
c_ders5 = "12:00 - 12:40"
c_ders6 = "13:50 - 14:30"
c_ders7 = "14:40 - 15:20"
c_ders8 = "15:30 - 16:10"




at = "\n"
ay = "\t"

pazartesi = at+m_arp+at+m_arp+at+dm3+at+dm3+at+adap+at+klm3+at+klm3+at+tde32+at+sctdt
sali = at+s_cog+at+s_cog+at+kur+at+kur+at+m_arp+at+beden1+at+tde32+at+tde32
carsamba = at+s_ted+at+s_ted+at+ink3+at+ink3+at+ing4+at+ing4+at+tde32+at+tde32
persembe = at+s_cog+at+s_cog+at+ikmt2+at+ikmt2+at+kdt+at+kdt+at+kur+at+sctdt
cuma =at+man+at+man+at+mat+at+mat+at+sctdt+at+sctdt+at+sfiko+at+sfiko

#Günler









print("12-B Sınıfı Ders Programı\nSürüm:\t",Version,"\n")

print(ders_list)

dongu_of_or_on = True

while dongu_of_or_on:

	ilk_girdi = input("\nHangi Günü incelemek istiyorsun?\n\n")

	if ilk_girdi == "pazartesi" or ilk_girdi == "PAZARTESİ" or ilk_girdi == "Pazartesi":
		print(pazartesi)
		

	elif ilk_girdi == "salı" or ilk_girdi == "SALI" or ilk_girdi == "Salı":
		print(sali)
		

	elif ilk_girdi == "çarşamba" or ilk_girdi == "ÇARŞAMBA" or ilk_girdi == "Çarşamba":
		print(carsamba)
		

	elif ilk_girdi == "perşembe" or ilk_girdi == "PERŞEMBE" or ilk_girdi == "Perşembe":
		print(persembe)
		
	elif ilk_girdi == "cuma" or ilk_girdi == "CUMA" or ilk_girdi == "Cuma":
		print(cuma)


		#Resetle
	elif ilk_girdi == "sil" or ilk_girdi == "SİL" or ilk_girdi == "Sil":
		print(at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at)
		print(at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at+at)
		print("12-B Sınıfı Ders Programı\nSürüm:\t",Version,"\n")
		print(ders_list)




	elif ilk_girdi == "Saat" or ilk_girdi == "SAAT" or ilk_girdi == "saat":
		print("Ders saatleri:")
		print("1\t\t2\t\t3\t\t4\t\t5\t\t6\t\t7\t\t8")
		print(ders1+ay+ders2+ay+ders3+ay+ders4+ay+ders5+ay+ders6+ay+ders7+ay+ders8)
		print(at)
		print("Cuma Günü:")
		print("1\t\t2\t\t3\t\t4\t\t5\t\t6\t\t7\t\t8")
		print(c_ders1+ay+c_ders2+ay+c_ders3+ay+c_ders4+ay+c_ders5+ay+c_ders6+ay+c_ders7+ay+c_ders8)
		print(at)


	elif ilk_girdi == "Yapımcı":
		print("\nYiğit Çıtak\n")

	elif ilk_girdi == "Kaynak kod":
		print("https://github.com/Yigit-2023/Ders_programi")
		
	else:
		print("\nLütfen Gün adı girin\n")
