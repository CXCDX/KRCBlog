# Karaca Blog Redesign: HTML Prototypes

Karaca.com/blog yeniden tasarım projesi kapsamında hazırlanan 11 sayfa HTML/CSS prototipi.

## Sayfalar

| # | Dosya | Sayfa Tipi | Açıklama |
|---|-------|-----------|----------|
| 01 | `01-anasayfa.html` | Anasayfa | Fade slider hero, 8 pillar nav, kategori filtreleri, 2-kolon grid + sidebar |
| 02 | `02-pillar-mutfak-pisirme.html` | Pillar | Mutfak & Pişirme hub sayfası, alt kategori pill'leri, featured article |
| 03 | `03-post-tarif.html` | TRF (Tarif) | Airfryer tarif formatı, recipe box, inline ürün kartı, FAQ accordion |
| 04 | `04-post-sorun-giderme.html` | SRN (Sorun Giderme) | Hatır kırmızı ışık çözümü, tanı tablosu, çözüm kartları, alert kutuları |
| 05 | `05-post-marka-hikayesi.html` | HIK (Hikaye) | 1973-2025 timeline, 5 era bölümü, inovasyon callout'ları |
| 06 | `06-post-karsilastirma.html` | KAR (Karşılaştırma) | BioDiamond vs Powersteel, VS hero, 10 satır comparison table, verdict |
| 07 | `07-post-rehber-airfryer.html` | REH (Rehber) | Airfryer satın alma rehberi, karar ağacı, 3-tier kartlar, özellik matrisi |
| 08 | `08-post-nasil-yapilir.html` | NAS (Nasıl Yapılır) | Biogranit bakım rehberi, 6 numaralı adım kartı, yapın/yapmayın grid |
| 09 | `09-post-ramazan-2026.html` | MVS (Mevsimsel) | Ramazan 2026 sofra rehberi, dark hero, 4 haftalık menü, bayram banneri |
| 10 | `10-arama-sonuclari.html` | Arama | Arama çubuğu, filtreli sonuç kartları, pagination, empty state |
| 11 | `11-404.html` | 404 | Kırık tabak illüstrasyonu, arama, popüler konu linkleri |

## Tasarım Sistemi

- **Renkler:** `--warm:#2c2420` `--gold:#b8956a` `--cream:#f7f3ee` `--sand:#e8e0d4`
- **Tipografi:** Playfair Display (serif, başlıklar) + DM Sans (sans-serif, body)
- **Layout:** max-width 1360px, responsive breakpoints 1100px / 768px / 480px
- **Bileşenler:** Tüm CSS tek dosya inline, JS IIFE pattern, sıfır bağımlılık

## Veri Kaynakları

- Ürün fiyatları: karaca.com (Şubat 2026)
- Marka tarihi: kurumsal kaynaklar, Arif Karaca röportajları
- Ramazan 2026: Diyanet takvimi (19 Şub - 20 Mar)
- Şikayetvar verileri: 41,747 Karaca şikayeti analizi

## Notlar

- Görseller SVG placeholder (cdn.karaca.com entegrasyonuna hazır)
- Schema markup ready: Recipe, FAQPage, HowTo, BreadcrumbList, Article, Product
- E-E-A-T sinyalleri: yazar bilgisi, kurum adı, tarih, güncelleme tarihi