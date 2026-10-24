from uzay_oyunu.dekoratorler import log_cagri, sinirla
from uzay_oyunu.komutlar import KOMUTLAR

# Görev 3 Uygulamaları
@log_cagri
def hedef_menusu(hedefler: list[str]) -> str:
    menu = "Nereye gitmek istersin?\n"
    for i, hedef in enumerate(hedefler, 1):
        menu += f"[{i}] {hedef}\n"
    return menu.strip()

@log_cagri
def galaksi_kur(gezegenler: list[str], baglantilar: dict, baslangic: str, **kwargs) -> dict:
    yakit = kwargs.get("yakit", 50)
    return {"gezegenler": gezegenler, "baglantilar": baglantilar, "konum": baslangic, "yakit": yakit}

# Görev 5 Uygulaması
@sinirla(0, 100)
def yakit_harca(miktar: int) -> int:
    return 100 - miktar

def travel(durum):
    while True:
        hedefler = durum.get("baglantilar", {}).get(durum.get("konum"), [])
        print(hedef_menusu(hedefler))
        girdi = input("> ").strip()
        
        # Görev 4 - Komut Sistemi Entegrasyonu
        if girdi in KOMUTLAR:
            komut_fonk, _ = KOMUTLAR[girdi]
            komut_fonk(durum)
            # Menüyü tekrar göstermek için döngü devam eder
            continue
        else:
            # Değilse eskisi gibi gezegen seçimi olarak yorumla
            return girdi
