import tkinter as tk

# --- DFA SINIFI (Mantık Kısmı) ---
# ---------------------------------------------------------
        # DFA DURUM (STATE) TANIMLARI:
        # q0  : Başlangıç durumu (Hiçbir şey okunmadı)
        # q1  : İl kodunun 1. rakamı okundu
        # q2  : İl kodunun 2. rakamı okundu (İl kodu tamamlandı)
        # q3  : İl kodundan sonraki BOŞLUK (Opsiyonel)
        # q4  : 1. Harf okundu
        # q5  : 2. Harf okundu
        # q6  : 3. Harf okundu (Maksimum harf sayısı)
        # q7  : Harflerden sonraki BOŞLUK
        # q8  : Son grubun 1. rakamı okundu (Kabul edilebilir durum)
        # q9  : Son grubun 2. rakamı okundu (Kabul edilebilir durum)
        # q10 : Son grubun 3. rakamı okundu (Kabul edilebilir durum)
        # q11 : Son grubun 4. rakamı okundu (Maksimum rakam sayısı)
        # ---------------------------------------------------------
class PlakaDFA:
    def __init__(self):
        self.current_state = 'q0'

    def is_digit(self, char):
        return '0' <= char <= '9'

    def is_letter(self, char):
        return 'A' <= char <= 'Z'
    
    def is_lowercase(self, char):
        return 'a' <= char <= 'z'

    def process_input(self, text):
        self.current_state = 'q0' 
        
        if not text:
            return False, "Giriş yapılmadı."

        for index, char in enumerate(text):
            if self.is_lowercase(char):
                return False, "Hata: Sadece BÜYÜK HARF kullanılmalıdır."

            # --- Durum Geçişleri ---
            if self.current_state == 'q0':
                if self.is_digit(char): self.current_state = 'q1'
                else: return False, "Hata: Plaka, il kodu (rakam) ile başlamalıdır."
                
            elif self.current_state == 'q1':
                if self.is_digit(char): self.current_state = 'q2'
                else: return False, "Hata: İl kodu 2 rakamdan oluşmalıdır."
                
            elif self.current_state == 'q2':
                if char == ' ': self.current_state = 'q3'
                elif self.is_letter(char): self.current_state = 'q4'
                elif self.is_digit(char): return False, "Hata: İl kodundan sonra rakam gelemez."
                else: return False, "Hata: İl kodundan sonra Harf veya Boşluk gelmelidir."
                
            elif self.current_state == 'q3':
                if self.is_letter(char): self.current_state = 'q4'
                else: return False, "Hata: Boşluktan sonra Harf gelmelidir."
            
            elif self.current_state == 'q4':
                if self.is_letter(char): self.current_state = 'q5'
                elif char == ' ': self.current_state = 'q7'
                elif self.is_digit(char): self.current_state = 'q8'
                else: return False, "Hata: Geçersiz karakter."

            elif self.current_state == 'q5':
                if self.is_letter(char): self.current_state = 'q6'
                elif char == ' ': self.current_state = 'q7'
                elif self.is_digit(char): self.current_state = 'q8'
                else: return False, "Hata: Geçersiz karakter."

            elif self.current_state == 'q6':
                if char == ' ': self.current_state = 'q7'
                elif self.is_digit(char): self.current_state = 'q8'
                elif self.is_letter(char): return False, "Hata: Harf grubu en fazla 3 karakter olabilir."
                else: return False, "Hata: Harflerden sonra Boşluk veya Rakam gelmelidir."

            elif self.current_state == 'q7':
                if self.is_digit(char): self.current_state = 'q8'
                elif self.is_letter(char): return False, "Hata: İki parça harf grubu olamaz."
                else: return False, "Hata: Son grup Rakam ile başlamalıdır."

            elif self.current_state == 'q8':
                if self.is_digit(char): self.current_state = 'q9'
                elif self.is_letter(char): return False, "Hata: Son kısımda harf bulunamaz."
                else: return False, "Hata: Son kısım rakam olmalıdır."

            elif self.current_state == 'q9':
                if self.is_digit(char): self.current_state = 'q10'
                elif self.is_letter(char): return False, "Hata: Son kısımda harf bulunamaz."

            elif self.current_state == 'q10':
                if self.is_digit(char): self.current_state = 'q11'
                elif self.is_letter(char): return False, "Hata: Son kısımda harf bulunamaz."
                
            elif self.current_state == 'q11':
                if self.is_digit(char): return False, "Hata: Son rakam grubu en fazla 4 basamak olabilir."
                else: return False, "Hata: Plaka formatı 4. rakamdan sonra bitmelidir."

        if self.current_state in ['q8', 'q9', 'q10', 'q11']:
            return True, "Geçerli Plaka"
        else:
            return False, "Hata: Plaka eksik girildi (Yarım kaldı)."

# --- ARAYÜZ KISMI (GUI) ---
def kontrol_et():
    plaka = entry_plaka.get()
    dfa = PlakaDFA()
    sonuc, mesaj = dfa.process_input(plaka)
    
    if sonuc:
        lbl_sonuc.config(text=f"{plaka} : {mesaj}", fg="green")
        lbl_hata.config(text="")
    else:
        lbl_sonuc.config(text=f"{plaka} : GEÇERSİZ", fg="red")
        lbl_hata.config(text=mesaj, fg="#d9534f")

# Renk Tanımları
ARKA_PLAN_RENGI = "#FFFACD"  # LemonChiffon (Hafif Sarı)

root = tk.Tk()
root.title("DFA Plaka Doğrulayıcı - ÖDEV")
root.geometry("450x300")
root.configure(bg=ARKA_PLAN_RENGI)  # Ana pencere arka planı

# Başlık
tk.Label(root, text="TR Plaka Doğrulama Sistemi", 
         font=("Arial", 14, "bold"), 
         bg=ARKA_PLAN_RENGI).pack(pady=15) # Label'ın arkasını da boyadık

# Giriş Çerçevesi
frame_giris = tk.Frame(root, bg=ARKA_PLAN_RENGI) # Çerçeve arkasını da boyadık
frame_giris.pack(pady=5)

tk.Label(frame_giris, text="Plaka Giriniz:", 
         font=("Arial", 12), 
         bg=ARKA_PLAN_RENGI).pack(side=tk.LEFT, padx=5)

entry_plaka = tk.Entry(frame_giris, font=("Arial", 12))
entry_plaka.pack(side=tk.LEFT, padx=5)

# Buton (Butonun rengi hafif gri kalsın ki belli olsun)
btn_kontrol = tk.Button(root, text="Doğrula", command=kontrol_et, 
                        font=("Arial", 11, "bold"), bg="#f0f0f0")
btn_kontrol.pack(pady=10)

# Sonuç Yazısı
lbl_sonuc = tk.Label(root, text="", font=("Arial", 12, "bold"), bg=ARKA_PLAN_RENGI)
lbl_sonuc.pack(pady=5)

# Detaylı Hata Yazısı
lbl_hata = tk.Label(root, text="", font=("Arial", 10, "italic"), fg="red", bg=ARKA_PLAN_RENGI)
lbl_hata.pack(pady=5)

root.mainloop()