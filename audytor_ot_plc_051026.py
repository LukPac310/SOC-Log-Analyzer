# 05 10 2026

import re
import datetime


# Pancerna konfiguracja portów OT (Modbus, Siemens S7, EtherNet/IP)
porty_krytyczne_plc = (502, 102, 44818)
czas_teraz = datetime.datetime.now().strftime("%Y-%m-$d %H:%M:%S")

try:
    with open("logi_plc_051026.txt", "r", encoding="utf-8") as plik_logow:
        surowy_tekst = plik_logow.read()

    # Wyciągamy pary (IP, Port) jako listę krotek i usuwamy duplikaty zbiorem set()
    wzorzec = r"SRC: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) DST_PORT: (\d+)"
    unikalne_wektory = set(re.findall(wzorzec, surowy_tekst))

    with open("raport_soc.txt", "a", encoding="utf-8") as plik_raportu:
        plik_raportu.write(f"\n*** AUDYT INFRASTRUKTURY OT/PLC dnia 05-10-2026: {czas_teraz} ***\n")

        for ip, port_tekst in unikalne_wektory:
            port = int(port_tekst)

            if port in porty_krytyczne_plc:
                plik_raportu.write(f"[ALARM OT!] Ingerencja w PLC z IP: {ip} na porcie: {port}\n")
            else:
                plik_raportu.write(f"[RUCH IT] Połączenie z IP: {ip} na port: {port}\n")
            # pass

    print("Audyt OT zakończony. Wyniki dopisano do raport_soc.txt")

except FileNotFoundError:
    print("BŁĄD: Brak pliku logi_plc_051026.txt!")

