#!/usr/bin/python3

from species.student import Student
from species.dziennik import Dziennik
from species.db import start_db


# Autor: Krzysztof Patelka
# Numer albumu: 117372
# Przedmiot: Języki obiektowe 1 (Python)
# Laboratorium nr 3 zadanie nr 3

BAZA_DANYCH = 'baza.db'
start_db(BAZA_DANYCH)


# Deklaracja funkcji main
def main():
    znak = 'a'
    while znak != 'x':
        print('--MENU--')
        print('a - dodaj studenta')
        print('b - przegladaj studentów')
        print('c - dodaj dziennik')
        print('d - przeglądaj dzienniki')
        print('---')
        print('e - przypisz ocene studentowi')
        print('f - wyświetl średnie oceny studentów')
        print('g - wyświetl oceny studenta')
        print('---')
        print('x - zakończ')
        znak = input('Wprowadź (a/b/c/d/e/f/g/x): ')
        if znak == 'a':
            print('---')
            print('Dodanie nowego studenta do bazy danych')
            student = Student(BAZA_DANYCH)
            student.podaj_imie()
            student.podaj_nazwisko()
            if student.zapisz_studenta():
                print('Student zopstał zapisany w bazie danych')
            else:
                print('Coś poszło nie tak przy zapisie do bazy danych')
            del student
            input('Naciśnij ENTER aby kontynuować')
        elif znak == 'b':
            print('---')
            print('Lista zapisanych studentów w bazie danych:')
            student = Student(BAZA_DANYCH)
            for wiersz in student.wczytaj_studentow():
                print('ID %2d: %s %s' % (wiersz[0], wiersz[1], wiersz[2]))
            del student
            input('Naciśnij ENTER aby kontynuować')
        elif znak == 'c':
            print('---')
            print('Dodanie nowego dziennika')
            dziennik = Dziennik(BAZA_DANYCH)
            dziennik.dodaj_nazwe_dziennika()
            if dziennik.zapisz_dziennik():
                print('Nowy dziennik został zapisany')
            else:
                print('Coś poszło nie tak przy zapisie do bazy danych')
            del dziennik
            input('Naciśnij ENTER aby kontynuować')
        elif znak == 'd':
            print('---')
            print('Lista dostepnych dzienników zapisanych w bazie danych')
            dziennik = Dziennik(BAZA_DANYCH)
            for wiersz in dziennik.wczytaj_dzienniki():
                print('ID dziennika %2d: %s' % (wiersz[0], wiersz[1]))
            del dziennik
            input('Naciśnij ENTER aby kontynuować')
        elif znak == 'e':
            print('---')
            print('Przypisanie oceny studentowi:')
            student = Student(BAZA_DANYCH)
            student.podaj_id()
            if student.zapisz_ocene():
                print('Ocena została przypisana studentowi')
            else:
                print('Coś poszło nie tak przy zapisie do bazy danych')
            del student
            input('Naciśnij ENTER aby kontynuować')
        elif znak == 'f':
            print('---')
            print('Średnia ocen uzyskanych przez studentów:')
            student = Student(BAZA_DANYCH)
            oceny = student.srednie_oceny()
            if oceny:
                for wiersz in oceny:
                    print('%s %s posiada średnią ocen: %.1f' % (wiersz[0], wiersz[1], wiersz[2]))
            else:
                print('Brak ocen')
            del student
            input('Naciśnij ENTER aby kontynuować')
        elif znak == 'g':
            print('---')
            print('Wyświetlanie ocen danego studenta:')
            student = Student(BAZA_DANYCH)
            student.podaj_id()
            oceny = student.oceny_studenta()
            if oceny:
                print('Oceny studenta %s %s' % (oceny[0][0], oceny[0][1]))
                id = 1
                for wiersz in oceny:
                    print('Ocena %2d: %d' % (id, wiersz[2]))
                    id += 1
            else:
                print('Podano niepoprawny ID studenta lub student nie posiada przypisanych ocen')
            del student
            input('Naciśnij ENTER aby kontynuować')


if __name__ == '__main__':
    main()
