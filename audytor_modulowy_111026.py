# 11/12 10 2026

import csv
import datetime

# 1. Importujemy konfigurację (dane wejściowe)
from konfiguracja_soc import PORTY_KRYTYCZNE_OT, PLIK_WEJSCIOWY, PLIK_WYNIKOWY_CSV

# 2. Importujemy narzędzie z zewn pliku (logikę ekstrakcji)
from skaner_funkcyjny import wyciagnij_wektory_z_logow

print("--- URUCHAMIANIE SYSTEMU SOC (WERSJA W PEŁNI MODUŁOWA)---")

# Używamy  wywołania funkcji z pliku zewn.
unikalne_wektory = wyciagnij_wektory_z_logow(PLIK_WEJSCIOWY)
czas_teraz = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

# Jeśli funkcja poprawnie zwróciła dane (zbiór nie jest pusty), przechodzimy do zapisu
if unikalne_wektory:
    with open(PLIK_WYNIKOWY_CSV, "w", newline="", encoding="utf-8") as plik_csv:
        pisarz_csv = csv.writer(plik_csv)
        pisarz_csv.writerow(["TIMESTAMP", "SOURCE_IP", "TARGET_PORT", "KLASYFIKACJA"])

        for ip, port_tekst in unikalne_wektory:
            port = int(port_tekst)

            if port in PORTY_KRYTYCZNE_OT:
                pisarz_csv.writerow([czas_teraz, ip, port, "ALARM_OT_PLC"])
            else:
                pisarz_csv.writerow([czas_teraz, ip, port, "RUCH_IT"])

    print(f"Audyt zakończony! Wygenerowano raport SIEM: {PLIK_WYNIKOWY_CSV}")
else:
    print("Brak danych do analizy. Sprawdź pliki logów.")       
