import pytest
from uzay_oyunu.dekoratorler import sure_olc, say, log_cagri, sinirla, hafiza

# Görev 1 Testleri
def test_sure_olc_sonuc_ve_isim_koruma(capsys):
    @sure_olc
    def topla(a, b=0):
        '''Toplama yapar.'''
        return a + b
    
    sonuc = topla(3, b=5)
    assert sonuc == 8
    assert topla.__name__ == "topla"
    assert topla.__doc__ == "Toplama yapar."
    
    captured = capsys.readouterr()
    assert "topla:" in captured.out
    assert "sn" in captured.out

# Görev 2 Testleri
def test_say():
    @say
    def test_fonk():
        pass
    test_fonk()
    test_fonk()
    assert test_fonk.cagri == 2

# Görev 3 Testleri
def test_log_cagri(capsys):
    @log_cagri
    def carp(x, y):
        return x * y
    
    carp(2, y=3)
    captured = capsys.readouterr()
    assert "-> carp(2, y=3)" in captured.out
    assert "<<- carp = 6" in captured.out

# Görev 5 Testleri
def test_sinirla():
    @sinirla(0, 100)
    def yakit_harca(miktar):
        return 100 - miktar
    
    assert yakit_harca(30) == 70
    assert yakit_harca(0) == 100
    assert yakit_harca(100) == 0
    
    with pytest.raises(ValueError, match="150 değeri 0-100 aralığında değil"):
        yakit_harca(150)
    with pytest.raises(ValueError):
        yakit_harca(-10)

# Bonus Testi
def test_hafiza():
    @hafiza(maxsize=2)
    def karesini_al(x):
        return x * x
    
    assert karesini_al(2) == 4
    assert karesini_al(3) == 9
    assert karesini_al(4) == 16
