# 05 10 2026


import re
import datetime
import csv # Nowy moduł wbudowany do obsługi tabel CSV

porty_ktytyczne_plc = (502, 102, 44818)
czas_teraz = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

try:
    with open("logi_plc_051026.txt", "r", encoding="utf-8") as plik_logow:
        surowy_tekst = plik_logow.read()

    wzorzec = r"SRC: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) DST_PORT: (\d+)"
    unikalne_wektory = set(re.findall(wzorzec, surowy_tekst))

    # Otwieram plik .csv do zapisu ("w"). Parametr newline="" zapobiega pustym liniom w Windowsie!
    with open("raport_siem_051026.csv", "w", newline="", encoding="utf-8") as plik_csv:
        # Tworze obiekt "pisarza CSV"
        pisarz_csv = csv.writer(plik_csv)

        # Zapisuje pierwszy wiersz tabeli: NAGŁÓWKI KOLUMN
        pisarz_csv.writerow(["TIMESTAMP", "SOURCE_IP", "TARGET_PORT", "KLASYFIKACJA"])

        # Przechodze za pomoca for przez incydenty i zapisujemy każdy jako osobny wiersz tabeli
        for ip, port_tekst in unikalne_wektory:
            port = int(port_tekst)

            if port in porty_ktytyczne_plc:
                pisarz_csv.writerow([czas_teraz, ip, port, "ALARM_OT_PLC"])
            else:
                pisarz_csv.writerow([czas_teraz, ip, port, "RUCH_IT"])

    print("Eksport zakończony! Sprawdź plik raport_siem_051026.csv")

except FileNotFoundError:
    print("Bład: Brak pliku z logami!")


