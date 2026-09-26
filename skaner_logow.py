import re

def ekstraktor_unikalnych_ip(surowy_log):
    # Wyciąga wszystkie adresy IP z tekstu i od razu konwertuje je na zbiór (usuwa duplikaty)
    wzorzec_ip = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    wszystkie_ip = re.findall(wzorzec_ip, surowy_log)
    return set(wszystkie_ip)

# 1. Definicja białej listy (adresy wojskowe/firmowe, których nie blokujemy)
bezpieczne_ip = {"10.0.0.5", "8.8.8.8", "1.1.1.1"}

# 2. Pusty słownik na ostateczną bazę do zablokowania
baza_zagrozen = {}

# 3. Główna logika skryptu
with open("incydenty.txt", "r") as plik_logow:
    caly_tekst = plik_logow.read()
    
    # Krok A: Wyciągnięcie unikalnych adresów z brudnych logów
    wynik_analizy = ekstraktor_unikalnych_ip(caly_tekst)
    
    # Krok B: Whitelisting (odfiltrowanie bezpiecznych adresów za pomocą matematyki na zbiorach)
    prawdziwe_zagrozenia = wynik_analizy - bezpieczne_ip
    
    # Krok C: Mapowanie zagrożeń do słownika
    for zagr in prawdziwe_zagrozenia:
        baza_zagrozen[zagr] = "ZABLOKOWANY"

# 4. Wyświetlenie gotowej blocklisty
print(f"Ostateczna baza zagrożeń do zablokowania:\n{baza_zagrozen}")