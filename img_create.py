from PIL import Image
import customtkinter as ctk

def add(label, image_path, size=(100, 100)):
    # Resmi yükle
    image = Image.open(image_path)
    
    # Resmi yeniden boyutlandır (ANTIALIAS yerine LANCZOS kullan)
    image = image.resize(size, Image.Resampling.LANCZOS)  # veya Image.LANCZOS
    
    # Resmi CTkImage formatına dönüştür
    ctk_image = ctk.CTkImage(image, size=size)
    
    # CTkLabel nesnesine resmi ekle
    label.configure(image=ctk_image)
    label.image = ctk_image  # Referansı koru