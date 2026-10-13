# 13 10 2026
# Poprawiony plik: zeby wyswietlal tylko nowe wektory
# Poprawiony plik: Rejestr Zdarzeń (Logowanie Alarmów)

import time
import datetime
from skaner_funkcyjny import wyciagnij_wektory_z_logow
from konfiguracja_soc import PLIK_WEJSCIOWY

print(f"Uruchamianie Strażnika SOC (Wciśnij Ctrl+C, aby zatrzymać)...")
print("Czekam na nowe incydenty...")

# 1. Pamiec strażnika - tworzymy pusty zbiór przed wejsciem do petli
znane_wektory = set()

while True:
    try:
        czas_teraz = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Pobieram to, co aktualnie znajduje się w pliku
        aktualne_wektory = wyciagnij_wektory_z_logow(PLIK_WEJSCIOWY)

        # 2. Matematyka zbiorow: Od aktualnych odejmujemy te, ktore juz mamy
        nowe_wektory = aktualne_wektory - znane_wektory

        # Jesli pojawilo sie cos nowego (zbior nie jest pusty), a wiec jest True to realizujemy instr. warunkowa
        if nowe_wektory:
            print(f"\n{czas_teraz} [ALARM] Wykryto nową aktywność ({len(nowe_wektory)} nowych zdarzeń):")

            with open("rejestr_alertow.txt", "a", encoding="utf-8") as plik_alertow:
                # 1. Dodajemy jedna pustą linię, aby odgrodzić NOWY BLOK od starych wpisów
                plik_alertow.write("\n")

                # 2. Pętla dopisuje kolejne adresy jeden pod drugim (bez przerw)
                for ip, port in nowe_wektory:
                    komunikat = f"--> Podejrzane IP: {ip} skanuje port: {port}"
                    print(komunikat) # Pokazanie na ekranie

                    plik_alertow.write(f"{czas_teraz} {komunikat}\n")

            # 3. Aktualizacja pamieci
            znane_wektory.update(nowe_wektory)

        time.sleep(5)

    except KeyboardInterrupt:
        print("\n[ZATRZYMANO] Oficer dyżurny zakończył dyżur SOC.")
        break # Instrukcja 'break' konczy petle while
 
