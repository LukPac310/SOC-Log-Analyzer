# 29 09 2026

import re
import datetime

# --- 1. MODUŁ EKSTRAKCJI ---
def ekstraktor_unikalnych_ip(surowy_log):
    wzorzec_ip = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    wszystkie_ip = re.findall(wzorzec_ip, surowy_log)
    return set(wszystkie_ip)

# --- 2. KONFIGURACJA ZAPORY I CZASU ---
bezpieczne_ip = {"10.0.0.5", "8.8.8.8", "1.1.1.1"}
czas_teraz = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# --- 3. ODCZYT I FILTROWANIE ---
with open("incydenty.txt", "r") as plik_logow:
    caly_tekst = plik_logow.read()
    
wykryte_ip = ekstraktor_unikalnych_ip(caly_tekst)
prawdziwe_zagrozenia = wykryte_ip - bezpieczne_ip

# --- 4. SYSTEM REAGOWANIA I RAPORTOWANIA ---
with open("raport_soc.txt", "a") as plik_raportu:
    plik_raportu.write(f"\n--- OSTATECZNY SKAN: {czas_teraz} ---\n")
    
    for adres_ip in prawdziwe_zagrozenia:
        if adres_ip == "192.168.1.10":
            plik_raportu.write(f"[KRYTYCZNY] Natychmiastowa blokada IP: {adres_ip}\n")
        else:
            plik_raportu.write(f"[PODEJRZANY] Dodano do monitoringu IP: {adres_ip}\n")

print("Silnik główny zakończył pracę. Raport wygenerowany.")