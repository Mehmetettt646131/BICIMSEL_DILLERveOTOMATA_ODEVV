# BICIMSEL_DILLERveOTOMATA_ODEVV
Plaka Doğrulama Otomat Uygulaması

Projenin Amacı
Bu projenin temel amacı, düzenli ifadeler (Regex) kullanmak yerine, bir string ifadenin geçerliliğini durumlar (states) ve geçişler (transitions) üzerinden analiz etmektir. Program, plakanın il kodunu, harf grubunu ve son rakam grubunu DFA kurallarına göre ayrıştırır.

Özellikler
DFA Tabanlı Doğrulama: Giriş stringini karakter karakter okur ve durumlar arasında geçiş yapar.
Görsel Arayüz (GUI): Python tkinter kütüphanesi ile kullanıcı dostu bir arayüz sunar.
Detaylı Hata Mesajları: Plakanın neden geçersiz olduğunu (Örn: "İl kodu 2 rakam olmalı", "Harf grubu en fazla 3 karakter olabilir") kullanıcıya bildirir.
Esnek Giriş: Boşluklu veya boşluksuz girişleri (Otomat mantığı dahilinde) yönetebilir.

Kullanılan Teknolojiler
Dil: Python 3.x
Arayüz: Tkinter (Python standart kütüphanesi)
Mantık: Finite Automata Theory (Sonlu Otomatlar Teorisi)

DFA Durum Diyagramı ve Mantığı
Sistem, toplam 12 durum (State) üzerinden çalışır. Her karakter girişinde otomat bir sonraki duruma geçer veya hata döndürür.
Durum (State),Açıklama
q0,                        Başlangıç Durumu.
q1 - q2,                   İl Kodu (2 Rakam) okuma aşaması.
q3,                        İl kodundan sonraki opsiyonel boşluk.
q4 - q6,                   "Harf Grubu (1, 2 veya 3 Harf) okuma aşaması."
q7,                        Harf grubundan sonraki opsiyonel boşluk.
q8 - q11,                  "Son Rakam Grubu (2, 3 veya 4 Rakam) okuma aşaması."
Kabul,"q8, q9, q10, q11    durumunda işlem biterse plaka GEÇERLİDİR."

<img width="875" height="198" alt="image" src="https://github.com/user-attachments/assets/0f453cab-646c-4634-819f-f511a4908ebf" />

Örnek Akış (Girdi: 34 AB 123)
3 okunur → q1'e geçilir.
4 okunur → q2'ye geçilir (İl kodu tamam).
(Boşluk) okunur → q3'e geçilir.
A okunur → q4'e geçilir.
B okunur → q5'e geçilir.
(Boşluk) okunur → q7'ye geçilir.
1 okunur → q8'e geçilir (Kabul durumu).
2 okunur → q9'a geçilir (Kabul durumu).
3 okunur → q10'a geçilir (Kabul durumu).



