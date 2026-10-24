import pytest
from uzay_oyunu.komutlar import komut, KOMUTLAR, yardim, envanter, harita

def test_komut_kayit():
    @komut("test_komutu", "test aciklamasi")
    def ornek(durum):
        pass
    
    assert "test_komutu" in KOMUTLAR
    assert KOMUTLAR["test_komutu"][1] == "test aciklamasi"
    assert KOMUTLAR["test_komutu"][0] is ornek
    
    # İki kez tanımlanırsa ValueError atmalı
    with pytest.raises(ValueError, match="zaten var"):
        @komut("test_komutu")
        def baska(durum):
            pass

def test_envanter(capsys):
    durum = {"credits": True, "engines": False, "copilot": True}
    envanter(durum)
    out, _ = capsys.readouterr()
    assert "Sende: bol kredi" in out
    assert "Sende: yetenekli bir pilot" in out
    assert "hiperdrive" not in out

def test_harita(capsys):
    durum = {
        "konum": "dünya",
        "baglantilar": {"dünya": ["centauri", "sirius"]}
    }
    harita(durum)
    out, _ = capsys.readouterr()
    assert "centauri, sirius" in out
