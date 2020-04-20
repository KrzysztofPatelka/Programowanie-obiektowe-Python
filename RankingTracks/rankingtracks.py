#!/usr/bin/python3

#Autor: Krzysztof Patelka
#Numer albumu: 117372
#Przedmiot: Języki obiektowe 1 (Python)
#Data ostatniej aktualizacji: 2020-03-17

#import modułów niezbędnych do działania programu
import pyodbc
from datetime import datetime
from time import time

#deklaracja stałych dotyczących połączenia z bazą danych
SERWER = 'localhost' 
BAZA_DANYCH = 'test' 
UZYTKOWNIK = 'test' 
HASLO = 'test'

#zapis pliku unique_tracks.txt do bazy danych
#plik zawiera 1 000 000 rekordów
def zapisz_unique_tracks():
    print("--")
    print("Zapis pliku unique_tracks.txt do bazy danych")
    try:
        filepatch = "unique_tracks.txt"
        plik = open(filepatch, "r", errors="ignore")
        polaczenie = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER="
                                    + SERWER
                                    + ";DATABASE="
                                    + BAZA_DANYCH
                                    + ";UID="
                                    + UZYTKOWNIK
                                    + ";PWD="
                                    + HASLO)
        cursor = polaczenie.cursor()
        print("Wykonywany jest zapis pliku unique_tracks.txt \
              do bazy danych. Proszę czekać.")
        for linia in plik:
            wiersz = linia.strip("\n").split("<SEP>")
            cursor.execute("""INSERT INTO unique_tracks \
                          (id_utworu, id_wykonania, artysta, tytul) \
                          VALUES (?,?,?,?)""",
                           wiersz[0], wiersz[1], wiersz[2], wiersz[3])
        polaczenie.commit()
        cursor.close()
        plik.close()
    except:
        print("Wystąpił błąd")
    input("Naciśnij ENTER aby kontynuować")
    print("--")

#zapis pliku triplets_sample_20p.txt do bazy danych
#plik zawiera 27 729 357 rekordów
def zapisz_triplets_sample_20p():
    print("--")
    print("Zapis pliku triplets_sample_20p.txt do bazy danych")
    try:
        filepatch = "triplets_sample_20p.txt"
        plik = open(filepatch, "r", errors="ignore")
        polaczenie = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER="
                                    + SERWER
                                    + ";DATABASE="
                                    + BAZA_DANYCH
                                    + ";UID="
                                    + UZYTKOWNIK
                                    + ";PWD="
                                    + HASLO)
        cursor = polaczenie.cursor()
        print("Wykonywany jest zapis pliku triplets_sample_20p.txt \
              do bazy danych. Proszę czekać.")
        for linia in plik:
            wiersz = linia.strip("\n").split("<SEP>")
            cursor.execute("""INSERT INTO triplets_sample_20p \
                           (id_uzytkownika, id_utworu, data_odsluchania) \
                           VALUES (?,?,?)""",
                           wiersz[0],
                           wiersz[1],
                           datetime.fromtimestamp(int(wiersz[2])))
        polaczenie.commit()
        cursor.close()
        plik.close()
    except:
        print("Wystąpił błąd")
    input("Naciśnij ENTER aby kontynuować")
    print("--")

#wyświetlanie artysty z najwiekszą liczbą odsłuchań
def artysta_z_najwieksza_liczba_odsluchan():
    print("--")
    print("Artysta z największą liczbą odsłuchań")
    print("Proszę czekać")
    try:
        polaczenie = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER="
                                    + SERWER + ";DATABASE="
                                    + BAZA_DANYCH
                                    + ";UID="
                                    + UZYTKOWNIK
                                    + ";PWD="
                                    + HASLO)
        cursor = polaczenie.cursor()
        czas_start = time()
        cursor.execute("SELECT TOP (1) unique_tracks.artysta, \
                       COUNT(unique_tracks.artysta) AS ilosc \
                       FROM triplets_sample_20p \
                       INNER JOIN unique_tracks \
                       ON unique_tracks.id_wykonania = \
                       triplets_sample_20p.id_utworu \
                       GROUP BY unique_tracks.artysta ORDER BY ilosc DESC")
        czas_koniec = time()
        wiersz = cursor.fetchone()
        print("Artysta %s został odsłuchany %s razy"
              % (wiersz[0], wiersz[1]))
        cursor.close()
        print("Czas przetwarzania zapytania: %.2f s"
              % (czas_koniec - czas_start))
    except:
        print("Wystąpił błąd")
    input("Naciśnij ENTER aby kontynuować")
    print("--")

#wyświetlanie 5 najpopularniejszych utworów
def piec_najpopularniejszych_utworow():
    print("--")
    print("5 najpopularniejszych utworów")
    print("Proszę czekać")
    try:
        polaczenie = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER="
                                    + SERWER
                                    + ";DATABASE="
                                    + BAZA_DANYCH
                                    + ";UID="
                                    + UZYTKOWNIK
                                    + ";PWD="
                                    + HASLO)
        cursor = polaczenie.cursor()
        czas_start = time()
        cursor.execute("SELECT TOP (5) COUNT(triplets_sample_20p.id_utworu) \
                       AS ilosc, unique_tracks.artysta, unique_tracks.tytul \
                       FROM triplets_sample_20p INNER JOIN unique_tracks \
                       ON triplets_sample_20p.id_utworu=unique_tracks.id_wykonania \
                       GROUP BY triplets_sample_20p.id_utworu, \
                       unique_tracks.artysta, unique_tracks.tytul \
                       ORDER BY ilosc DESC")
        czas_koniec = time()
        licznik = 1
        for wiersz in cursor:
            print("Miejsce %s utwór %s, wykonawcy %s został odsłuchany %s razy"
                  % (licznik, wiersz[2], wiersz[1], wiersz[0]))
            licznik = licznik +1
        cursor.close()
        print("Czas przetwarzania zapytania: %.2f s"
              % (czas_koniec - czas_start))
    except:
        print("Wystąpił błąd")
    input("Naciśnij ENTER aby kontynuować")
    print("--")

#definicja main()
def main():
    znak = "a"
    while znak != "x":
        print("--MENU--")
        print("a - zapis pliku unique_tracks.txt do bazy danych")
        print("b - zapis pliku triplets_sample_20p.txt do bazy danych")
        print("c - artysta z największą liczbą odsłuchań")
        print("d - 5 najpopularniejszych utworów")
        print("x - wyjście z programu")
        znak = input("Wprowadź (a/b/c/d/x): ")
        print("--")
        if znak == "a":
            zapisz_unique_tracks()
        elif znak == "b":
            zapisz_triplets_sample_20p()
        elif znak == "c":
            artysta_z_najwieksza_liczba_odsluchan()
        elif znak == "d":
            piec_najpopularniejszych_utworow()

if __name__ == "__main__":
    main()
