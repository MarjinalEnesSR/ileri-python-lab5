import time
from functools import wraps

# Görev 1 - Süre ölçen dekoratör
def sure_olc(fonksiyon):
    @wraps(fonksiyon)
    def sarmalayici(*args, **kwargs):
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.perf_counter()
        print(f"{fonksiyon.__name__}: {bitis - baslangic:.4f} sn")
        return sonuc
    return sarmalayici

# Görev 2 - Çağrı sayacı
def say(fonksiyon):
    @wraps(fonksiyon)
    def sarmalayici(*args, **kwargs):
        sarmalayici.cagri += 1
        return fonksiyon(*args, **kwargs)
    sarmalayici.cagri = 0
    return sarmalayici

# Görev 3 - Loglayan dekoratör
def log_cagri(fonksiyon):
    @wraps(fonksiyon)
    def sarmalayici(*args, **kwargs):
        args_str = ", ".join([repr(a) for a in args])
        kwargs_str = ", ".join([f"{k}={repr(v)}" for k, v in kwargs.items()])
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))
        
        print(f"-> {fonksiyon.__name__}({all_args})")
        sonuc = fonksiyon(*args, **kwargs)
        print(f"<<- {fonksiyon.__name__} = {repr(sonuc)}")
        return sonuc
    return sarmalayici

# Görev 5 - Argüman alan dekoratör
def sinirla(alt, ust):
    def dekorator(fonksiyon):
        @wraps(fonksiyon)
        def sarmalayici(*args, **kwargs):
            if not args:
                return fonksiyon(*args, **kwargs)
            deger = args[0]
            if not (alt <= deger <= ust):
                raise ValueError(f"{fonksiyon.__name__}: {deger} değeri {alt}-{ust} aralığında değil")
            return fonksiyon(*args, **kwargs)
        return sarmalayici
    return dekorator

# Bonus - lru_cache kullanmadan hafıza
def hafiza(maxsize=None):
    def dekorator(fonksiyon):
        cache = {}
        @wraps(fonksiyon)
        def sarmalayici(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            if key in cache:
                return cache[key]
            sonuc = fonksiyon(*args, **kwargs)
            cache[key] = sonuc
            
            if maxsize is not None and len(cache) > maxsize:
                # dict insertion order (Python 3.7+) sayesinde ilk ekleneni buluruz
                ilk_anahtar = next(iter(cache))
                del cache[ilk_anahtar]
                
            return sonuc
        return sarmalayici
    return dekorator
