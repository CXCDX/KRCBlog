import os

# Shared head/styles/nav/footer for all pages
def shared_head(title):
    return f'''<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Karaca Dergi</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800&family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;0,9..144,600;0,9..144,700;1,9..144,300;1,9..144,400&display=swap" rel="stylesheet">'''

SHARED_VARS = '''
:root{
  --bk:#111;--g900:#1a1a1a;--g700:#333;--g500:#666;--g400:#888;--g300:#aaa;--g200:#ccc;--g100:#e5e5e5;--g50:#f5f5f5;
  --white:#fff;--accent:#e63946;--accent-soft:#fef1f2;
  --serif:'Fraunces',Georgia,serif;
  --sans:'Plus Jakarta Sans',-apple-system,sans-serif;
  --ease:cubic-bezier(.22,1,.36,1);
  --max:1440px;--content:800px;--pad:clamp(20px,4vw,80px)
}
'''

SHARED_BASE = '''
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-font-smoothing:antialiased}
body{font-family:var(--sans);color:var(--bk);background:var(--white);line-height:1.6;overflow-x:hidden}
a{text-decoration:none;color:inherit;transition:color .2s}
img{display:block;max-width:100%;height:auto}
'''

SHARED_NAV_CSS = '''
.topbar{background:var(--bk);color:var(--white);text-align:center;padding:10px var(--pad);font-size:12px;font-weight:500;letter-spacing:.08em;text-transform:uppercase}
.topbar a{color:var(--white);text-decoration:underline;text-underline-offset:2px}
.nav{position:sticky;top:0;z-index:100;background:rgba(255,255,255,.97);backdrop-filter:blur(12px);border-bottom:1px solid var(--g100)}
.nav-inner{max-width:var(--max);margin:0 auto;padding:0 var(--pad);display:flex;align-items:center;justify-content:space-between;height:64px}
.nav-logo{font-family:var(--serif);font-size:22px;font-weight:600;letter-spacing:-.02em}
.nav-logo span{font-weight:300;color:var(--g400);margin-left:6px;font-size:16px}
.nav-links{display:flex;align-items:center;gap:32px}
.nav-links a{font-size:13px;font-weight:500;color:var(--g500);letter-spacing:.02em;transition:color .2s}
.nav-links a:hover{color:var(--bk)}
.nav-icons{display:flex;gap:16px;align-items:center}
.nav-icons a{color:var(--g500)}
.nav-icons a:hover{color:var(--bk)}
.nav-icons svg{width:20px;height:20px}
'''

SHARED_FOOTER_CSS = '''
.footer{background:var(--bk);color:var(--white);padding:64px 0 32px}
.ft-inner{max-width:var(--max);margin:0 auto;padding:0 var(--pad)}
.ft-grid{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:48px;margin-bottom:48px}
.ft-brand{font-family:var(--serif);font-size:24px;font-weight:600;margin-bottom:16px}
.ft-brand span{font-weight:300;color:var(--g400);font-size:16px;margin-left:4px}
.ft-desc{font-size:13px;color:var(--g400);line-height:1.6;max-width:300px}
.ft-col h4{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--g400);margin-bottom:16px}
.ft-col a{display:block;font-size:13px;color:var(--g300);margin-bottom:10px;transition:color .2s}
.ft-col a:hover{color:var(--white)}
.ft-bottom{border-top:1px solid rgba(255,255,255,.1);padding-top:24px;display:flex;justify-content:space-between;align-items:center;font-size:12px;color:var(--g500)}
.ft-socials{display:flex;gap:16px}
.ft-socials a{color:var(--g400);transition:color .2s}
.ft-socials a:hover{color:var(--white)}
@media(max-width:1024px){.ft-grid{grid-template-columns:1fr 1fr}}
@media(max-width:640px){.nav-links{display:none}.ft-grid{grid-template-columns:1fr}}
'''

NAV_HTML = '''
<div class="topbar">2.500 TL uezeri alisverislerde uecretsiz kargo &middot; <a href="https://www.karaca.com">karaca.com</a></div>
<nav class="nav">
  <div class="nav-inner">
    <a href="01-anasayfa.html" class="nav-logo">Karaca <span>Dergi</span></a>
    <div class="nav-links">
      <a href="02-pillar-mutfak-pisirme.html">Mutfak &amp; Pisirme</a>
      <a href="08-post-nasil-yapilir.html">Sofra &amp; Sunum</a>
      <a href="04-post-sorun-giderme.html">Kahve &amp; Cay</a>
      <a href="07-post-rehber-airfryer.html">Kuecuek Ev Aletleri</a>
      <a href="08-post-nasil-yapilir.html">Bakim &amp; Destek</a>
      <a href="05-post-marka-hikayesi.html">Hikayemiz</a>
    </div>
    <div class="nav-icons">
      <a href="10-arama-sonuclari.html"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg></a>
      <a href="https://www.karaca.com"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4zM3 6h18M16 10a4 4 0 01-8 0"/></svg></a>
    </div>
  </div>
</nav>
'''

FOOTER_HTML = '''
<footer class="footer">
  <div class="ft-inner">
    <div class="ft-grid">
      <div>
        <div class="ft-brand">Karaca <span>Dergi</span></div>
        <p class="ft-desc">Mutfak, sofra ve yasama dair ilham veren icerikler. 1973'ten bu yana paylasacak cok seyimiz var.</p>
      </div>
      <div class="ft-col">
        <h4>Icerikler</h4>
        <a href="03-post-tarif.html">Tarifler</a>
        <a href="07-post-rehber-airfryer.html">Rehberler</a>
        <a href="06-post-karsilastirma.html">Karsilastirmalar</a>
        <a href="08-post-nasil-yapilir.html">Bakim Ipuclari</a>
        <a href="09-post-ramazan-2026.html">Mevsimsel</a>
      </div>
      <div class="ft-col">
        <h4>Karaca</h4>
        <a href="05-post-marka-hikayesi.html">Hikayemiz</a>
        <a href="https://www.karaca.com/magazalar">Magazalar</a>
        <a href="https://www.karaca.com/kariyer">Kariyer</a>
        <a href="https://www.karaca.com/iletisim">Iletisim</a>
      </div>
      <div class="ft-col">
        <h4>Yasal</h4>
        <a href="https://www.karaca.com/kvkk">KVKK Aydinlatma</a>
        <a href="https://www.karaca.com/cerez-politikasi">Cerez Politikasi</a>
        <a href="https://www.karaca.com/kullanim-kosullari">Kullanim Kosullari</a>
      </div>
    </div>
    <div class="ft-bottom">
      <span>&copy; 2026 Karaca Zueccaciye A.S.</span>
      <div class="ft-socials">
        <a href="https://www.instagram.com/karaca/">Instagram</a>
        <a href="https://www.youtube.com/karaca">YouTube</a>
        <a href="https://www.pinterest.com/karaca/">Pinterest</a>
        <a href="https://www.karaca.com">karaca.com</a>
      </div>
    </div>
  </div>
</footer>
'''

print("Shared components ready. Use these in page generation.")
print(f"NAV_HTML length: {len(NAV_HTML)}")
print(f"FOOTER_HTML length: {len(FOOTER_HTML)}")
