# Dekoratör Sırası ve Kapsam Analizi

## Fibonacci (fib) Çağrı Sayıları
- **Yalnızca @say:** 21891
- **@say üstte, @lru_cache altta:** 39
- **@lru_cache üstte, @say altta:** 21

## Neden Farklılar?
Dekoratörlerin yerleştirilme sırası (yukarıdan aşağıya), sarmalayıcıların birbirini içe doğru sarma sırasını belirler.

1. **Yalnızca @say:** Önbellek kullanılmadığı için `fib(20)` hesaplanırken her düğümde alt kollar tekrar tekrar hesaplanır ve üstel bir çağrı sayısı (21891) ortaya çıkar.
2. **@say üstte, @lru_cache altta:** Hiyerarşi `@say -> @lru_cache -> fonksiyon` şeklindedir. `fib()` her çağrıldığında önce dıştaki `say` dekoratörü sayacı artırır, sonra `lru_cache` devreye girer. Yani `say`, "önbelleğe yapılan isabetli (hit) ve isabetsiz (miss) tüm sorguları" sayar. 20 ana hesaplama + 19 önbellek isabeti = 39 kez tetiklenir.
3. **@lru_cache üstte, @say altta:** Hiyerarşi `@lru_cache -> @say -> fonksiyon` şeklindedir. Fonksiyon çağrıldığında önce `lru_cache` kontrol yapar. Eğer sonuç önbellekte varsa `lru_cache` doğrudan sonucu döner ve içerdeki `say` sarmalayıcısına **hiç uğramaz**. Bu yüzden `say` sadece önbellekte bulunmayan "gerçek" hesaplamalar yapıldığında sayar. 0'dan 20'ye kadar 21 farklı değer ilk kez hesaplandığı için çağrı sayısı yalnızca 21'de kalır.
