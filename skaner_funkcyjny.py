# 11 10 2026

import re

# 1. DEFINICJA NASZEGO WŁASNEGO NARZĘDZIA (FUNKCJI)
def wyciagnij_wektory_z_logow(sciezka_do_pliku):
    """Funkcja czyta plik logów i zwraca zbiór unikalnych krotek (IP, Port)"""
    try:
        with open(sciezka_do_pliku, "r", encoding="utf-8") as plik:
            tekst = plik.read()

        wzorzec = r"SRC: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) DST_PORT: (\d+)"
        surowe_krotki = re.findall(wzorzec, tekst)

        # return - najważniejsze słowo w funkcji! 
        # Przekazuje ono gotowy wynik z powrotem do miejsca, z którego funkcję wywołano.
        return set(surowe_krotki)

    except FileNotFoundError:
        print(f"BŁĄD: Nie można zmaleźć pliku {sciezka_do_pliku}")
        # Jeśli pliku nie ma, zwracamy pusty zbiór, żeby program się nie zawiesił
        return set()


# 2. GŁÓWNA CZĘŚĆ PROGRAMU (WYWOŁANIE FUNKCJI) W TARCZY OCHRONNEJ
if __name__ == "__main__":
    print("--- TEST NASZEJ WŁASNEJ FUNKCJI ---")

    # Odpalamy naszą funkcję i podajemy jej konkretny plik,
    # a to, co funkcja nam zwróci (wynik działania 'return'), łapiemy do zmiennej.
    unikalne_incydenty = wyciagnij_wektory_z_logow("logi_plc_051026.txt")

    # Sprawdzamy, czy funkcja poprawnie oddała nam dane:
    print(f"Zbiór zwrócony przez funkcję zawiera {len(unikalne_incydenty)} unikalnych wektorów ataków: \n")

    for ip, port in unikalne_incydenty:
        print(f"- Znaleziono adres IP: {ip} kierujący się na port: {port}")

        

