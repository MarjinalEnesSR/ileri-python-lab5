# Görev 4 - Komut sistemi: kayıt deseni

KOMUTLAR = {}

def komut(ad, aciklama=""):
    def dekorator(fonksiyon):
        if ad in KOMUTLAR:
            raise ValueError(f"'{ad}' adında bir komut zaten var!")
        # Fonksiyonu değiştirmeden (fonksiyon, aciklama) olarak kaydediyoruz
        KOMUTLAR[ad] = (fonksiyon, aciklama)
        return fonksiyon
    return dekorator

@komut("yardim", "komutları listeler")
def yardim(durum):
    for k_adi, (_, k_aciklama) in KOMUTLAR.items():
        print(f"{k_adi:<10} {k_aciklama}")

@komut("envanter", "envanter eşyalarını gösterir")
def envanter(durum):
    esya_var = False
    if durum.get("credits"):
        print("Sende: bol kredi")
        esya_var = True
    if durum.get("engines"):
        print("Sende: hiperdrive")
        esya_var = True
    if durum.get("copilot"):
        print("Sende: yetenekli bir pilot")
        esya_var = True
    if not esya_var:
        print("Envanter boş.")

@komut("harita", "gidebileceğin gezegenleri gösterir")
def harita(durum):
    konum = durum.get("konum")
    baglantilar = durum.get("baglantilar", {})
    hedefler = baglantilar.get(konum, [])
    print(", ".join(hedefler))
