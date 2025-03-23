import customtkinter as ctk
import img_create
import data
import indirme_motoru
from os import path, listdir, system

kullanici_dizini = path.expanduser("~")

def widget(window):
	# Dış yüzey Fonksiyonları
	def program_hakkinda_button_funk():
		def geri():
			tema_secme_imlecler.pack(pady=120,padx=20)
			program_hakkinda.pack_forget()
			program_hakkinda_button.configure(command=program_hakkinda_button_funk, text="Hakkında")

		program_hakkinda_button.configure(command=geri, text="Geri")
		tema_secme_imlecler.pack_forget()
		program_hakkinda.pack(pady=120,padx=20)

	# Dış yüzey
	program_hakkinda_button = ctk.CTkButton(window,text="Hakkında",font=("italic",20),width=60,command=program_hakkinda_button_funk,fg_color="#20b2aa",text_color="white",hover_color="#90ee90")
	program_hakkinda_button.place(y=10,x=10)

	kullanici_ismi = ctk.CTkLabel(window,text=f"Merhaba {data.Kullanici_tam_adi}",font=("italic",30),text_color="white")
	kullanici_ismi.pack(pady=3)


	#Ana Sayfa: İmleçler
	tema_secme_imlecler = ctk.CTkScrollableFrame(window,fg_color="#00bfff",width=1400,height=800)
	tema_secme_imlecler.pack(pady=120,padx=20)

	# İmleç içerik: Fonksionlar
	def imlec_no1_funk_indir(url=data.imlec_no1_url):
		dizin = f"{kullanici_dizini}/.icons"
		indirme_motoru.dosya_indir(url)
		indirme_motoru.arsiv_cikar("file.zip",dizin)
		imlec_urun_no1_button_indir.place_forget()
		imlec_urun_no1_button_kaldir.place(x=650,y=30)

	def imlec_no1_funk_kaldir():
		system(f"rm -rf {kullanici_dizini}/.icons/Naroz-vr2b")
		imlec_urun_no1_button_kaldir.place_forget()
		imlec_urun_no1_button_indir.place(x=650,y=30)

	def imlec_no2_funk_indir(url=data.imlec_no2_url):
		dizin = f"{kullanici_dizini}/.icons"
		indirme_motoru.dosya_indir(url)
		indirme_motoru.arsiv_cikar("file.zip",dizin)
		imlec_urun_no2_button_indir.place_forget()
		imlec_urun_no2_button_kaldir.place(x=650,y=30)

	def imlec_no2_funk_kaldir():
		system(f"rm -rf {kullanici_dizini}/.icons/miku-cursor-linux")
		imlec_urun_no2_button_kaldir.place_forget()
		imlec_urun_no2_button_indir.place(x=650,y=30)

	def imlec_no3_funk_indir(url=data.imlec_no3_url):
		dizin = f"{kullanici_dizini}/.icons"
		indirme_motoru.dosya_indir(url)
		indirme_motoru.arsiv_cikar("file.zip",dizin)
		imlec_urun_no3_button_indir.place_forget()
		imlec_urun_no3_button_kaldir.place(x=650,y=30)

	def imlec_no3_funk_kaldir():
		system(f"rm -rf {kullanici_dizini}/.icons/Apple-cursors")
		imlec_urun_no3_button_kaldir.place_forget()
		imlec_urun_no3_button_indir.place(x=650,y=30)

	def imlec_no4_funk_indir(url=data.imlec_no4_url):
		dizin = f"{kullanici_dizini}/.icons"
		indirme_motoru.dosya_indir(url)
		indirme_motoru.arsiv_cikar("file.zip",dizin)
		imlec_urun_no4_button_indir.place_forget()
		imlec_urun_no4_button_kaldir.place(x=650,y=30)

	def imlec_no4_funk_kaldir():
		system(f"rm -rf {kullanici_dizini}/.icons/Onedark-pixel")
		imlec_urun_no4_button_kaldir.place_forget()
		imlec_urun_no4_button_indir.place(x=650,y=30)

	def imlec_no5_funk_indir(url=data.imlec_no5_url):
		dizin = f"{kullanici_dizini}/.icons"
		indirme_motoru.dosya_indir(url)
		indirme_motoru.arsiv_cikar("file.zip",dizin)
		imlec_urun_no5_button_indir.place_forget()
		imlec_urun_no5_button_kaldir.place(x=650,y=30)

	def imlec_no5_funk_kaldir():
		system(f"rm -rf {kullanici_dizini}/.icons/We10XOS-cursors")
		imlec_urun_no5_button_kaldir.place_forget()
		imlec_urun_no5_button_indir.place(x=650,y=30)

	def imlec_no6_funk_indir(url=data.imlec_no6_url):
		dizin = f"{kullanici_dizini}/.icons"
		indirme_motoru.dosya_indir(url)
		indirme_motoru.arsiv_cikar("file.zip",dizin)
		imlec_urun_no6_button_indir.place_forget()
		imlec_urun_no6_button_kaldir.place(x=650,y=30)

	def imlec_no6_funk_kaldir():
		system(f"rm -rf {kullanici_dizini}/.icons/Candy-Pixel-Blue-vr2")
		imlec_urun_no6_button_kaldir.place_forget()
		imlec_urun_no6_button_indir.place(x=650,y=30)

	def imlec_no7_funk_indir(url=data.imlec_no7_url):
		dizin = f"{kullanici_dizini}/.icons"
		indirme_motoru.dosya_indir(url)
		indirme_motoru.arsiv_cikar("file.zip",dizin)
		imlec_urun_no7_button_indir.place_forget()
		imlec_urun_no7_button_kaldir.place(x=650,y=30)

	def imlec_no7_funk_kaldir():
		system(f"rm -rf {kullanici_dizini}/.icons/Kureiji-Ollie-v2")
		imlec_urun_no7_button_kaldir.place_forget()
		imlec_urun_no7_button_indir.place(x=650,y=30)

	def imlec_no8_funk_indir(url=data.imlec_no8_url):
		dizin = f"{kullanici_dizini}/.icons"
		indirme_motoru.dosya_indir(url)
		indirme_motoru.arsiv_cikar("file.zip",dizin)
		imlec_urun_no8_button_indir.place_forget()
		imlec_urun_no8_button_kaldir.place(x=650,y=30)

	def imlec_no8_funk_kaldir():
		system(f"rm -rf {kullanici_dizini}/.icons/BreezeX-Light")
		imlec_urun_no8_button_kaldir.place_forget()
		imlec_urun_no8_button_indir.place(x=650,y=30)

	def imlec_no9_funk_indir(url=data.imlec_no9_url):
		dizin = f"{kullanici_dizini}/.icons"
		indirme_motoru.dosya_indir(url)
		indirme_motoru.arsiv_cikar("file.zip",dizin)
		imlec_urun_no9_button_indir.place_forget()
		imlec_urun_no9_button_kaldir.place(x=650,y=30)

	def imlec_no9_funk_kaldir():
		system(f"rm -rf {kullanici_dizini}/.icons/Lighted-Pixel-Blue-vr2")
		imlec_urun_no9_button_kaldir.place_forget()
		imlec_urun_no9_button_indir.place(x=650,y=30)

	def imlec_no10_funk_indir(url=data.imlec_no10_url):
		dizin = f"{kullanici_dizini}/.icons"
		indirme_motoru.dosya_indir(url)
		indirme_motoru.arsiv_cikar("file.zip",dizin)
		imlec_urun_no10_button_indir.place_forget()
		imlec_urun_no10_button_kaldir.place(x=650,y=30)

	def imlec_no10_funk_kaldir():
		system(f"rm -rf {kullanici_dizini}/.icons/Banana")
		imlec_urun_no10_button_kaldir.place_forget()
		imlec_urun_no10_button_indir.place(x=650,y=30)

	def imlec_no11_funk_indir(url=data.imlec_no11_url):
		dizin = f"{kullanici_dizini}/.icons"
		indirme_motoru.dosya_indir(url)
		indirme_motoru.arsiv_cikar("file.zip",dizin)
		imlec_urun_no11_button_indir.place_forget()
		imlec_urun_no11_button_kaldir.place(x=650,y=30)

	def imlec_no11_funk_kaldir():
		system(f"rm -rf {kullanici_dizini}/.icons/Bibata-Modern-Amber")
		imlec_urun_no11_button_kaldir.place_forget()
		imlec_urun_no11_button_indir.place(x=650,y=30)

	def imlec_no12_funk_indir(url=data.imlec_no12_url):
		dizin = f"{kullanici_dizini}/.icons"
		indirme_motoru.dosya_indir(url)
		indirme_motoru.arsiv_cikar("file.zip",dizin)
		imlec_urun_no12_button_indir.place_forget()
		imlec_urun_no12_button_kaldir.place(x=650,y=30)

	def imlec_no12_funk_kaldir():
		system(f"rm -rf {kullanici_dizini}/.icons/taiga-cursor")
		imlec_urun_no12_button_kaldir.place_forget()
		imlec_urun_no12_button_indir.place(x=650,y=30)

	# İmleç sayfası içeriği 

	#İmleç 1
	imlec_urun_no1 = ctk.CTkFrame(tema_secme_imlecler,height=200,width=1000,fg_color=data.UrunTema_ozellikleri["panel__fg_color"])
	imlec_urun_no1.pack(pady=20)
	
	imlec_urun_no1_title = ctk.CTkLabel(imlec_urun_no1,text="Naroz Cursor",font=("italic",40),text_color=data.UrunTema_ozellikleri["urun_adi__text_color"])
	imlec_urun_no1_title.place(x=250,y=30)
	
	if  "Naroz-vr2b" in listdir(f"{kullanici_dizini}/.icons/"):
		imlec_urun_no1_button_kaldir = ctk.CTkButton(imlec_urun_no1,text="Kaldır",font=("italic",30),height=100,command=imlec_no1_funk_kaldir,fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])
		imlec_urun_no1_button_kaldir.place(x=650,y=30)

		imlec_urun_no1_button_indir = ctk.CTkButton(imlec_urun_no1,text="İndir",font=("italic",30),height=100,command=imlec_no1_funk_indir)
	else:
		imlec_urun_no1_button_indir = ctk.CTkButton(imlec_urun_no1,text="İndir",font=("italic",30),height=100,command=imlec_no1_funk_indir)
		imlec_urun_no1_button_indir.place(x=650,y=30)

		imlec_urun_no1_button_kaldir = ctk.CTkButton(imlec_urun_no1,text="Kaldır",font=("italic",30),height=100,command=imlec_no1_funk_kaldir,fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])

	imlec_urun_no1_img = ctk.CTkLabel(imlec_urun_no1,text="",)
	img_create.add(label=imlec_urun_no1_img,image_path="IMG/imlecler/no1_icon.png",size=(140,140))
	imlec_urun_no1_img.place(x=10,y=35)

	imlec_urun_no1_aciklama = ctk.CTkLabel(imlec_urun_no1,text=data.imlec_no1_aciklama,font=("italic",10),text_color=data.UrunTema_ozellikleri["urun_aciklama__text_color"])	
	imlec_urun_no1_aciklama.place(x=230,y=90)

	#İmleç 2
	imlec_urun = ctk.CTkFrame(tema_secme_imlecler,height=200,width=1000,fg_color=data.UrunTema_ozellikleri["panel__fg_color"])
	imlec_urun.pack(pady=20)
	
	imlec_urun_title = ctk.CTkLabel(imlec_urun,text="Miku Cursors",font=("italic",40),text_color=data.UrunTema_ozellikleri["urun_adi__text_color"])
	imlec_urun_title.place(x=250,y=30)
	
	if  "miku-cursor-linux" in listdir(f"{kullanici_dizini}/.icons/"):
		imlec_urun_no2_button_kaldir = ctk.CTkButton(imlec_urun,text="Kaldır",font=("italic",30),height=100,command=imlec_no2_funk_kaldir,fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])
		imlec_urun_no2_button_kaldir.place(x=650,y=30)

		imlec_urun_no2_button_indir = ctk.CTkButton(imlec_urun,text="İndir",font=("italic",30),height=100,command=imlec_no2_funk_indir)
	else:
		imlec_urun_no2_button_indir = ctk.CTkButton(imlec_urun,text="İndir",font=("italic",30),height=100,command=imlec_no2_funk_indir)
		imlec_urun_no2_button_indir.place(x=650,y=30)

		imlec_urun_no2_button_kaldir = ctk.CTkButton(imlec_urun,text="Kaldır",font=("italic",30),height=100,command=imlec_no2_funk_kaldir,fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])

	imlec_urun_img = ctk.CTkLabel(imlec_urun,text="",)
	img_create.add(label=imlec_urun_img,image_path="IMG/imlecler/no2_icon.png",size=(140,140))
	imlec_urun_img.place(x=10,y=35)

	imlec_urun_aciklama = ctk.CTkLabel(imlec_urun,text=data.imlec_no2_aciklama,font=("italic",10),text_color=data.UrunTema_ozellikleri["urun_aciklama__text_color"])	
	imlec_urun_aciklama.place(x=230,y=90)

	#İmleç 3
	imlec_urun = ctk.CTkFrame(tema_secme_imlecler,height=200,width=1000,fg_color=data.UrunTema_ozellikleri["panel__fg_color"])
	imlec_urun.pack(pady=20)
	
	imlec_urun_title = ctk.CTkLabel(imlec_urun,text="Apple Cursors",font=("italic",40),text_color=data.UrunTema_ozellikleri["urun_adi__text_color"])
	imlec_urun_title.place(x=250,y=30)
	
	if  "Apple-cursors" in listdir(f"{kullanici_dizini}/.icons/"):
		imlec_urun_no3_button_kaldir = ctk.CTkButton(imlec_urun,text="Kaldır",font=("italic",30),height=100,command=imlec_no3_funk_kaldir,fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])
		imlec_urun_no3_button_kaldir.place(x=650,y=30)

		imlec_urun_no3_button_indir = ctk.CTkButton(imlec_urun,text="İndir",font=("italic",30),height=100,command=imlec_no3_funk_indir)
	else:
		imlec_urun_no3_button_indir = ctk.CTkButton(imlec_urun,text="İndir",font=("italic",30),height=100,command=imlec_no3_funk_indir)
		imlec_urun_no3_button_indir.place(x=650,y=30)

		imlec_urun_no3_button_kaldir = ctk.CTkButton(imlec_urun,text="Kaldır",font=("italic",30),height=100,command=imlec_no3_funk_kaldir,fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])

	imlec_urun_img = ctk.CTkLabel(imlec_urun,text="",)
	img_create.add(label=imlec_urun_img,image_path="IMG/imlecler/no3_icon.png",size=(140,140))
	imlec_urun_img.place(x=10,y=35)

	imlec_urun_aciklama = ctk.CTkLabel(imlec_urun,text=data.imlec_no3_aciklama,font=("italic",10),text_color=data.UrunTema_ozellikleri["urun_aciklama__text_color"])	
	imlec_urun_aciklama.place(x=230,y=90)

	#İmleç 4
	imlec_urun = ctk.CTkFrame(tema_secme_imlecler,height=200,width=1000,fg_color=data.UrunTema_ozellikleri["panel__fg_color"])
	imlec_urun.pack(pady=20)
	
	imlec_urun_title = ctk.CTkLabel(imlec_urun,text="Onedark Pixel",font=("italic",40),text_color=data.UrunTema_ozellikleri["urun_adi__text_color"])
	imlec_urun_title.place(x=250,y=30)
	
	if  "Onedark-pixel" in listdir(f"{kullanici_dizini}/.icons/"):
		imlec_urun_no4_button_kaldir = ctk.CTkButton(imlec_urun,text="Kaldır",font=("italic",30),height=100,command=imlec_no4_funk_kaldir,fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])
		imlec_urun_no4_button_kaldir.place(x=650,y=30)

		imlec_urun_no4_button_indir = ctk.CTkButton(imlec_urun,text="İndir",font=("italic",30),height=100,command=imlec_no4_funk_indir)
	else:
		imlec_urun_no4_button_indir = ctk.CTkButton(imlec_urun,text="İndir",font=("italic",30),height=100,command=imlec_no4_funk_indir)
		imlec_urun_no4_button_indir.place(x=650,y=30)

		imlec_urun_no4_button_kaldir = ctk.CTkButton(imlec_urun,text="Kaldır",font=("italic",30),height=100,command=imlec_no4_funk_kaldir,fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])

	imlec_urun_img = ctk.CTkLabel(imlec_urun,text="",)
	img_create.add(label=imlec_urun_img,image_path="IMG/imlecler/no4_icon.png",size=(140,140))
	imlec_urun_img.place(x=10,y=35)

	imlec_urun_aciklama = ctk.CTkLabel(imlec_urun,text=data.imlec_no4_aciklama,font=("italic",10),text_color=data.UrunTema_ozellikleri["urun_aciklama__text_color"])	
	imlec_urun_aciklama.place(x=230,y=90)

	#İmleç 5
	imlec_urun = ctk.CTkFrame(tema_secme_imlecler,height=200,width=1000,fg_color=data.UrunTema_ozellikleri["panel__fg_color"])
	imlec_urun.pack(pady=20)
	
	imlec_urun_title = ctk.CTkLabel(imlec_urun,text="We10XOS",font=("italic",40),text_color=data.UrunTema_ozellikleri["urun_adi__text_color"])
	imlec_urun_title.place(x=250,y=30)
	
	if  "We10XOS-cursors" in listdir(f"{kullanici_dizini}/.icons/"):
		imlec_urun_no5_button_kaldir = ctk.CTkButton(imlec_urun,text="Kaldır",font=("italic",30),height=100,command=imlec_no5_funk_kaldir,fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])
		imlec_urun_no5_button_kaldir.place(x=650,y=30)

		imlec_urun_no5_button_indir = ctk.CTkButton(imlec_urun,text="İndir",font=("italic",30),height=100,command=imlec_no5_funk_indir)
	else:
		imlec_urun_no5_button_indir = ctk.CTkButton(imlec_urun,text="İndir",font=("italic",30),height=100,command=imlec_no5_funk_indir)
		imlec_urun_no5_button_indir.place(x=650,y=30)

		imlec_urun_no5_button_kaldir = ctk.CTkButton(imlec_urun,text="Kaldır",font=("italic",30),height=100,command=imlec_no5_funk_kaldir,fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])

	imlec_urun_img = ctk.CTkLabel(imlec_urun,text="",)
	img_create.add(label=imlec_urun_img,image_path="IMG/imlecler/no5_icon.png",size=(140,140))
	imlec_urun_img.place(x=10,y=35)

	imlec_urun_aciklama = ctk.CTkLabel(imlec_urun,text=data.imlec_no5_aciklama,font=("italic",10),text_color=data.UrunTema_ozellikleri["urun_aciklama__text_color"])	
	imlec_urun_aciklama.place(x=230,y=90)

	#İmleç 6
	imlec_urun = ctk.CTkFrame(tema_secme_imlecler,height=200,width=1000,fg_color=data.UrunTema_ozellikleri["panel__fg_color"])
	imlec_urun.pack(pady=20)
	
	imlec_urun_title = ctk.CTkLabel(imlec_urun,text="Candy Pixel",font=("italic",40),text_color=data.UrunTema_ozellikleri["urun_adi__text_color"])
	imlec_urun_title.place(x=250,y=30)
	
	if  "Candy-Pixel-Blue-vr2" in listdir(f"{kullanici_dizini}/.icons/"):
		imlec_urun_no6_button_kaldir = ctk.CTkButton(imlec_urun,text="Kaldır",font=("italic",30),height=100,command=imlec_no6_funk_kaldir,fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])
		imlec_urun_no6_button_kaldir.place(x=650,y=30)

		imlec_urun_no6_button_indir = ctk.CTkButton(imlec_urun,text="İndir",font=("italic",30),height=100,command=imlec_no6_funk_indir)
	else:
		imlec_urun_no6_button_indir = ctk.CTkButton(imlec_urun,text="İndir",font=("italic",30),height=100,command=imlec_no6_funk_indir)
		imlec_urun_no6_button_indir.place(x=650,y=30)

		imlec_urun_no6_button_kaldir = ctk.CTkButton(imlec_urun,text="Kaldır",font=("italic",30),height=100,command=imlec_no6_funk_kaldir,fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])

	imlec_urun_img = ctk.CTkLabel(imlec_urun,text="",)
	img_create.add(label=imlec_urun_img,image_path="IMG/imlecler/no6_icon.png",size=(140,140))
	imlec_urun_img.place(x=10,y=35)

	imlec_urun_aciklama = ctk.CTkLabel(imlec_urun,text=data.imlec_no6_aciklama,font=("italic",10),text_color=data.UrunTema_ozellikleri["urun_aciklama__text_color"])	
	imlec_urun_aciklama.place(x=230,y=90)

	#İmleç 7
	imlec_urun = ctk.CTkFrame(tema_secme_imlecler,height=200,width=1000,fg_color=data.UrunTema_ozellikleri["panel__fg_color"])
	imlec_urun.pack(pady=20)
	
	imlec_urun_title = ctk.CTkLabel(imlec_urun,text="Kureiji Ollie",font=("italic",40),text_color=data.UrunTema_ozellikleri["urun_adi__text_color"])
	imlec_urun_title.place(x=250,y=30)
	
	if  "Kureiji-Ollie-v2" in listdir(f"{kullanici_dizini}/.icons/"):
		imlec_urun_no7_button_kaldir = ctk.CTkButton(imlec_urun,text="Kaldır",font=("italic",30),height=100,command=imlec_no7_funk_kaldir,fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])
		imlec_urun_no7_button_kaldir.place(x=650,y=30)

		imlec_urun_no7_button_indir = ctk.CTkButton(imlec_urun,text="İndir",font=("italic",30),height=100,command=imlec_no7_funk_indir)
	else:
		imlec_urun_no7_button_indir = ctk.CTkButton(imlec_urun,text="İndir",font=("italic",30),height=100,command=imlec_no7_funk_indir)
		imlec_urun_no7_button_indir.place(x=650,y=30)

		imlec_urun_no7_button_kaldir = ctk.CTkButton(imlec_urun,text="Kaldır",font=("italic",30),height=100,command=imlec_no7_funk_kaldir,fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])

	imlec_urun_img = ctk.CTkLabel(imlec_urun,text="",)
	img_create.add(label=imlec_urun_img,image_path="IMG/imlecler/no7_icon.png",size=(140,140))
	imlec_urun_img.place(x=10,y=35)

	imlec_urun_aciklama = ctk.CTkLabel(imlec_urun,text=data.imlec_no7_aciklama,font=("italic",10),text_color=data.UrunTema_ozellikleri["urun_aciklama__text_color"])	
	imlec_urun_aciklama.place(x=230,y=90)

	#İmleç 8
	imlec_urun = ctk.CTkFrame(tema_secme_imlecler,height=200,width=1000,fg_color=data.UrunTema_ozellikleri["panel__fg_color"])
	imlec_urun.pack(pady=20)
	
	imlec_urun_title = ctk.CTkLabel(imlec_urun,text="BreezeX Light",font=("italic",40),text_color=data.UrunTema_ozellikleri["urun_adi__text_color"])
	imlec_urun_title.place(x=250,y=30)
	
	if  "BreezeX-Light" in listdir(f"{kullanici_dizini}/.icons/"):
		imlec_urun_no8_button_kaldir = ctk.CTkButton(imlec_urun,text="Kaldır",font=("italic",30),height=100,command=imlec_no8_funk_kaldir,fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])
		imlec_urun_no8_button_kaldir.place(x=650,y=30)

		imlec_urun_no8_button_indir = ctk.CTkButton(imlec_urun,text="İndir",font=("italic",30),height=100,command=imlec_no8_funk_indir)
	else:
		imlec_urun_no8_button_indir = ctk.CTkButton(imlec_urun,text="İndir",font=("italic",30),height=100,command=imlec_no8_funk_indir)
		imlec_urun_no8_button_indir.place(x=650,y=30)

		imlec_urun_no8_button_kaldir = ctk.CTkButton(imlec_urun,text="Kaldır",font=("italic",30),height=100,command=imlec_no8_funk_kaldir,fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])

	imlec_urun_img = ctk.CTkLabel(imlec_urun,text="",)
	img_create.add(label=imlec_urun_img,image_path="IMG/imlecler/no8_icon.png",size=(140,140))
	imlec_urun_img.place(x=10,y=35)

	imlec_urun_aciklama = ctk.CTkLabel(imlec_urun,text=data.imlec_no8_aciklama,font=("italic",10),text_color=data.UrunTema_ozellikleri["urun_aciklama__text_color"])	
	imlec_urun_aciklama.place(x=230,y=90)

	#İmleç 9
	imlec_urun = ctk.CTkFrame(tema_secme_imlecler,height=200,width=1000,fg_color=data.UrunTema_ozellikleri["panel__fg_color"])
	imlec_urun.pack(pady=20)
	
	imlec_urun_title = ctk.CTkLabel(imlec_urun,text="Lighted Pixel Blue",font=("italic",30),text_color=data.UrunTema_ozellikleri["urun_adi__text_color"])
	imlec_urun_title.place(x=250,y=30)
	
	if  "Lighted-Pixel-Blue-vr2" in listdir(f"{kullanici_dizini}/.icons/"):
		imlec_urun_no9_button_kaldir = ctk.CTkButton(imlec_urun,text="Kaldır",font=("italic",30),height=100,command=imlec_no9_funk_kaldir,fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])
		imlec_urun_no9_button_kaldir.place(x=650,y=30)

		imlec_urun_no9_button_indir = ctk.CTkButton(imlec_urun,text="İndir",font=("italic",30),height=100,command=imlec_no9_funk_indir)
	else:
		imlec_urun_no9_button_indir = ctk.CTkButton(imlec_urun,text="İndir",font=("italic",30),height=100,command=imlec_no9_funk_indir)
		imlec_urun_no9_button_indir.place(x=650,y=30)

		imlec_urun_no9_button_kaldir = ctk.CTkButton(imlec_urun,text="Kaldır",font=("italic",30),height=100,command=imlec_no9_funk_kaldir,fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])

	imlec_urun_img = ctk.CTkLabel(imlec_urun,text="",)
	img_create.add(label=imlec_urun_img,image_path="IMG/imlecler/no9_icon.png",size=(140,140))
	imlec_urun_img.place(x=10,y=35)

	imlec_urun_aciklama = ctk.CTkLabel(imlec_urun,text=data.imlec_no9_aciklama,font=("italic",10),text_color=data.UrunTema_ozellikleri["urun_aciklama__text_color"])	
	imlec_urun_aciklama.place(x=230,y=90)

	#İmleç 10
	imlec_urun = ctk.CTkFrame(tema_secme_imlecler,height=200,width=1000,fg_color=data.UrunTema_ozellikleri["panel__fg_color"])
	imlec_urun.pack(pady=20)
	
	imlec_urun_title = ctk.CTkLabel(imlec_urun,text="Banana",font=("italic",40),text_color=data.UrunTema_ozellikleri["urun_adi__text_color"])
	imlec_urun_title.place(x=250,y=30)
	
	if  "Banana" in listdir(f"{kullanici_dizini}/.icons/"):
		imlec_urun_no10_button_kaldir = ctk.CTkButton(imlec_urun,text="Kaldır",font=("italic",30),height=100,command=imlec_no10_funk_kaldir,fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])
		imlec_urun_no10_button_kaldir.place(x=650,y=30)

		imlec_urun_no10_button_indir = ctk.CTkButton(imlec_urun,text="İndir",font=("italic",30),height=100,command=imlec_no10_funk_indir)
	else:
		imlec_urun_no10_button_indir = ctk.CTkButton(imlec_urun,text="İndir",font=("italic",30),height=100,command=imlec_no10_funk_indir)
		imlec_urun_no10_button_indir.place(x=650,y=30)

		imlec_urun_no10_button_kaldir = ctk.CTkButton(imlec_urun,text="Kaldır",font=("italic",30),height=100,command=imlec_no10_funk_kaldir,fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])

	imlec_urun_img = ctk.CTkLabel(imlec_urun,text="",)
	img_create.add(label=imlec_urun_img,image_path="IMG/imlecler/no10_icon.png",size=(140,140))
	imlec_urun_img.place(x=10,y=35)

	imlec_urun_aciklama = ctk.CTkLabel(imlec_urun,text=data.imlec_no10_aciklama,font=("italic",10),text_color=data.UrunTema_ozellikleri["urun_aciklama__text_color"])	
	imlec_urun_aciklama.place(x=230,y=90)

	#İmleç 11
	imlec_urun = ctk.CTkFrame(tema_secme_imlecler,height=200,width=1000,fg_color=data.UrunTema_ozellikleri["panel__fg_color"])
	imlec_urun.pack(pady=20)
	
	imlec_urun_title = ctk.CTkLabel(imlec_urun,text="Bibata Modern Amber",font=("italic",40),text_color=data.UrunTema_ozellikleri["urun_adi__text_color"])
	imlec_urun_title.place(x=170,y=30)
	
	if  "Bibata-Modern-Amber" in listdir(f"{kullanici_dizini}/.icons/"):
		imlec_urun_no11_button_kaldir = ctk.CTkButton(imlec_urun,text="Kaldır",font=("italic",30),height=100,command=imlec_no11_funk_kaldir,fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])
		imlec_urun_no11_button_kaldir.place(x=650,y=30)

		imlec_urun_no11_button_indir = ctk.CTkButton(imlec_urun,text="İndir",font=("italic",30),height=100,command=imlec_no11_funk_indir)
	else:
		imlec_urun_no11_button_indir = ctk.CTkButton(imlec_urun,text="İndir",font=("italic",30),height=100,command=imlec_no11_funk_indir)
		imlec_urun_no11_button_indir.place(x=650,y=30)

		imlec_urun_no11_button_kaldir = ctk.CTkButton(imlec_urun,text="Kaldır",font=("italic",30),height=100,command=imlec_no11_funk_kaldir,fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])

	imlec_urun_img = ctk.CTkLabel(imlec_urun,text="",)
	img_create.add(label=imlec_urun_img,image_path="IMG/imlecler/no11_icon.png",size=(140,140))
	imlec_urun_img.place(x=10,y=35)

	imlec_urun_aciklama = ctk.CTkLabel(imlec_urun,text=data.imlec_no11_aciklama,font=("italic",10),text_color=data.UrunTema_ozellikleri["urun_aciklama__text_color"])	
	imlec_urun_aciklama.place(x=230,y=90)

	#İmleç 12
	imlec_urun = ctk.CTkFrame(tema_secme_imlecler,height=200,width=1000,fg_color=data.UrunTema_ozellikleri["panel__fg_color"])
	imlec_urun.pack(pady=20)
	
	imlec_urun_title = ctk.CTkLabel(imlec_urun,text="Taiga Cursor",font=("italic",40),text_color=data.UrunTema_ozellikleri["urun_adi__text_color"])
	imlec_urun_title.place(x=250,y=30)
	
	if  "taiga-cursor" in listdir(f"{kullanici_dizini}/.icons/"):
		imlec_urun_no12_button_kaldir = ctk.CTkButton(imlec_urun,text="Kaldır",font=("italic",30),height=100,command=imlec_no12_funk_kaldir,fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])
		imlec_urun_no12_button_kaldir.place(x=650,y=30)

		imlec_urun_no12_button_indir = ctk.CTkButton(imlec_urun,text="İndir",font=("italic",30),height=100,command=imlec_no12_funk_indir)
	else:
		imlec_urun_no12_button_indir = ctk.CTkButton(imlec_urun,text="İndir",font=("italic",30),height=100,command=imlec_no12_funk_indir)
		imlec_urun_no12_button_indir.place(x=650,y=30)

		imlec_urun_no12_button_kaldir = ctk.CTkButton(imlec_urun,text="Kaldır",font=("italic",30),height=100,command=imlec_no12_funk_kaldir,fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])

	imlec_urun_img = ctk.CTkLabel(imlec_urun,text="",)
	img_create.add(label=imlec_urun_img,image_path="IMG/imlecler/no12_icon.png",size=(140,140))
	imlec_urun_img.place(x=10,y=35)

	imlec_urun_aciklama = ctk.CTkLabel(imlec_urun,text=data.imlec_no12_aciklama,font=("italic",10),text_color=data.UrunTema_ozellikleri["urun_aciklama__text_color"])	
	imlec_urun_aciklama.place(x=230,y=90)


	#Ana Sayfa: Hakkında
	program_hakkinda = ctk.CTkScrollableFrame(window,fg_color="#00bfff",width=1400,height=800)
	#program_hakkinda.pack(pady=120,padx=20)

	tema_secme_ikon_title = ctk.CTkLabel(program_hakkinda,text=data.program_hakkinda,font=("italic",40),text_color="white")
	tema_secme_ikon_title.pack(pady=40)