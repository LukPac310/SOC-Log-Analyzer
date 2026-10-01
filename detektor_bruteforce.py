# 01 10 2026

import re
import datetime

bezpieczne_ip = {"10.0.0.5", "8.8.8.8", "1.1.1.1"}
prog_alarmowy = 3
czas_teraz = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 1. Wczytanie surowego pliku logów
with open("incydenty.txt", "r") as plik_logow:
    caly_tekst = plik_logow.read()

# 2. Wyciągnięcie WSZYSTKICH wystąpień IP (lista z duplikatami)
wzorzec_ip = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
wszystkie_wystapienia_ip = re.findall(wzorzec_ip, caly_tekst)

# 3. Odfiltrowanie bezpiecznych adresów (zbiór unikalnych podejrzanych IP)
podejrzane_unikalne_ip = set(wszystkie_wystapienia_ip) - bezpieczne_ip

# 4. Zliczanie uderzeń dla każdego podejrzanego IP
statystyki_atakow = {}

for ip in podejrzane_unikalne_ip:
    statystyki_atakow[ip] = wszystkie_wystapienia_ip.count(ip)

# 5. Zapisanie wyników analizy Brute-Force do raportu
with open("raport_soc.txt", "a") as plik_raportu:
    plik_raportu.write(f"\n--- SKAN BRUTE-FORCE: {czas_teraz} ---\n")
    
    for ip, liczba_uderzen in statystyki_atakow.items():
        if liczba_uderzen >= prog_alarmowy:
            plik_raportu.write(f"[ALARM BRUTE-FORCE] IP: {ip} | Próby: {liczba_uderzen} -> BLOKADA!\n")
        else:
            plik_raportu.write(f"[INFO] IP: {ip} | Próby: {liczba_uderzen} -> Poniżej progu.\n")
        # pass

print("Analiza Brute-Force zakończona. Sprawdź plik raport_soc.txt!")