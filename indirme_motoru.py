import os
import requests
import zipfile
import data

def arsiv_cikar(zip_dosya_yolu, cikarilacak_dizin):
    """
    ZIP dosyasını belirtilen dizine çıkarır.

    :param zip_dosya_yolu: Çıkarılacak ZIP dosyasının tam yolu.
    :param cikarilacak_dizin: Dosyaların çıkarılacağı hedef dizin.
    """
    try:
        # Dizin yoksa oluştur
        if not os.path.exists(cikarilacak_dizin):
            os.makedirs(cikarilacak_dizin)

        # ZIP dosyasını aç ve çıkar
        with zipfile.ZipFile(zip_dosya_yolu, 'r') as zipf:
            zipf.extractall(cikarilacak_dizin)
            #print(f"{zip_dosya_yolu} dosyası {cikarilacak_dizin} dizinine başarıyla çıkarıldı.")
    except zipfile.BadZipFile:
        print("Hata: Geçersiz ZIP dosyası.")
    except FileNotFoundError:
        print("Hata: ZIP dosyası bulunamadı.")
    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")

def dosya_indir(url, dosya_adi="file.zip"):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(dosya_adi, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    #print(f"{dosya_adi} başarıyla indirildi.")


def internet_var_mi():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        pass
    return False

