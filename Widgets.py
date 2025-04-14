import customtkinter as ctk
import img_create
import data
import indirme_motoru
from os import path, listdir, system
import time
from threading import Thread
from tqdm import tqdm 

kullanici_dizini = path.expanduser("~")

def widget(window):
	# Dış yüzey Fonksiyonları
	def program_hakkinda_button_funk():
		def geri():
			tema_secme_imlecler.pack(pady=120,padx=20)
			program_hakkinda.pack_forget()
			program_hakkinda_button.configure(command=program_hakkinda_button_funk, text="About")

		program_hakkinda_button.configure(command=geri, text="Back")
		tema_secme_imlecler.pack_forget()
		program_hakkinda.pack(pady=120,padx=20)

	# Dış yüzey
	program_hakkinda_button = ctk.CTkButton(window,text="About",font=("italic",20),width=60,command=program_hakkinda_button_funk,fg_color="#20b2aa",text_color="white",hover_color="#90ee90")
	program_hakkinda_button.place(y=10,x=10)

	kullanici_ismi = ctk.CTkLabel(window,text=f"Hello {data.Kullanici_tam_adi}",font=("italic",30),text_color="white")
	kullanici_ismi.pack(pady=3)


	#Ana Sayfa: İmleçler
	tema_secme_imlecler = ctk.CTkScrollableFrame(window,fg_color="#00bfff",width=1400,height=800)
	tema_secme_imlecler.pack(pady=120,padx=20)

	# İmleç içerik: Fonksionlar
	def imlec_span(urun_name, urun_code_name, urun_index, url):
		def imlec_funk_indir(url=url):
			imlec_urun_no1_button_indir.place_forget()
			progressbar.place(x=650, y=30)
			progressbar.set(0)
          
			def indirme_thread():
				try:
					dizin = f"{kullanici_dizini}/.icons"
                    
                    # Animasyonlu ilerleme göstergesi
					for i in range(0, 81, 5):
						progressbar.set(i/100)
						tema_secme_imlecler.update()
						time.sleep(0.1)
                    
                    # Gerçek indirme işlemi
					indirme_motoru.dosya_indir(url)
					indirme_motoru.arsiv_cikar("file.zip", dizin)
                    
                    # Kalan kısmı tamamla
					for i in range(85, 101, 5):
						progressbar.set(i/100)
						tema_secme_imlecler.update()
						time.sleep(0.05)
                    
					progressbar.place_forget()
					imlec_urun_no1_button_kaldir.place(x=650, y=30)
                
				except Exception as e:
					print(f"İndirme hatası: {e}")
					progressbar.place_forget()
					imlec_urun_no1_button_indir.place(x=650, y=30)

			Thread(target=indirme_thread, daemon=True).start()

		def imlec_funk_kaldir():
			imlec_urun_no1_button_kaldir.place_forget()
			progressbar.place(x=650, y=30)
			progressbar.set(0)
            
			def kaldirma_thread():
				try:
					for i in range(1, 101):
						time.sleep(0.02)
						progressbar.set(i/100)
						tema_secme_imlecler.update()
                    
					system(f"rm -rf {kullanici_dizini}/.icons/{urun_code_name}")
					progressbar.place_forget()
					imlec_urun_no1_button_indir.place(x=650, y=30)
				except Exception as e:
					print(f"Kaldırma hatası: {e}")
					progressbar.place_forget()
					imlec_urun_no1_button_kaldir.place(x=650, y=30)

			Thread(target=kaldirma_thread, daemon=True).start()

        # Main panel
		imlec_urun = ctk.CTkFrame(tema_secme_imlecler, height=200, width=1000,
			fg_color=data.UrunTema_ozellikleri["panel__fg_color"])
		imlec_urun.pack(pady=20)

        # Icon
		imlec_urun_img = ctk.CTkLabel(imlec_urun, text="")
		img_create.add(label=imlec_urun_img, image_path=f"IMG/imlecler/no{urun_index}_icon.png",
			size=(140,140))
		imlec_urun_img.place(x=10, y=35)

        # Title
		imlec_urun_title = ctk.CTkLabel(imlec_urun, text=urun_name, font=("italic",40), 
			text_color=data.UrunTema_ozellikleri["urun_adi__text_color"])
		imlec_urun_title.place(x=200, y=50)

        # Progress bar
		progressbar = ctk.CTkProgressBar(imlec_urun, width=300, height=30)
		progressbar.set(0)

        # Buttons
		if urun_code_name in listdir(f"{kullanici_dizini}/.icons/"):
			imlec_urun_no1_button_kaldir = ctk.CTkButton(
				imlec_urun, text="Kaldır", font=("italic",30), height=100,
				command=imlec_funk_kaldir,
				fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],
				hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])
			imlec_urun_no1_button_kaldir.place(x=650, y=30)

			imlec_urun_no1_button_indir = ctk.CTkButton(
				imlec_urun, text="İndir", font=("italic",30), height=100,
				command=imlec_funk_indir)
		else:
			imlec_urun_no1_button_indir = ctk.CTkButton(
				imlec_urun, text="İndir", font=("italic",30), height=100,
				command=imlec_funk_indir)
			imlec_urun_no1_button_indir.place(x=650, y=30)

			imlec_urun_no1_button_kaldir = ctk.CTkButton(
				imlec_urun, text="Kaldır", font=("italic",30), height=100,
				command=imlec_funk_kaldir,
				fg_color=data.UrunTema_ozellikleri["kaldir_buton__fg_color"],
				hover_color=data.UrunTema_ozellikleri["kaldir_buton__hover_color"])
	
	# İmleç sayfası içeriği 

	#İmleçler
	imlec_span(urun_name="Naroz Cursor",urun_code_name="Naroz-vr2b",urun_index="1",url=data.imlec_no1_url)
	imlec_span(urun_name="Miku Cursor",urun_code_name="miku-cursor-linux",urun_index="2",url=data.imlec_no2_url)
	imlec_span(urun_name="Apple Cursors",urun_code_name="Apple-cursors",urun_index="3",url=data.imlec_no3_url)
	imlec_span(urun_name="Onedark Pixel",urun_code_name="Onedark-pixel",urun_index="4",url=data.imlec_no4_url)
	imlec_span(urun_name="We10XOS Cursors",urun_code_name="We10XOS-cursors",urun_index="5",url=data.imlec_no5_url)
	imlec_span(urun_name="Candy Pixel Cursor",urun_code_name="Candy-Pixel-Blue-vr2",urun_index="6",url=data.imlec_no6_url)
	imlec_span(urun_name="Kureiji Ollie",urun_code_name="Kureiji-Ollie-v2",urun_index="7",url=data.imlec_no7_url)
	imlec_span(urun_name="BreezeX-Light",urun_code_name="BreezeX-Light",urun_index="8",url=data.imlec_no8_url)
	imlec_span(urun_name="Aydınlatılmış Piksel",urun_code_name="Lighted-Pixel-Blue-vr2",urun_index="9",url=data.imlec_no9_url)
	imlec_span(urun_name="Banana",urun_code_name="Banana",urun_index="10",url=data.imlec_no10_url)
	imlec_span(urun_name="Bibata Modern Amber",urun_code_name="Bibata-Modern-Amber",urun_index="11",url=data.imlec_no11_url)
	imlec_span(urun_name="taiga-cursor",urun_code_name="taiga-cursor",urun_index="12",url=data.imlec_no12_url)


	#Ana Sayfa: Hakkında
	program_hakkinda = ctk.CTkScrollableFrame(window,fg_color="#00bfff",width=1400,height=800)
	#program_hakkinda.pack(pady=120,padx=20)

	tema_secme_ikon_title = ctk.CTkLabel(program_hakkinda,text=data.program_hakkinda,font=("italic",40),text_color="white")
	tema_secme_ikon_title.pack(pady=40)