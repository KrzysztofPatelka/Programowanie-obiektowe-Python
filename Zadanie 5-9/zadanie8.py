#!/usr/bin/python3

#Autor: Krzysztof Patelka
#Numer albumu: 117372
#Przedmiot: Języki obiektowe 1 (Python)
#Zadanie numer 8

from functools import wraps

#deklaracja stałych
ILE_WYWOLAN_FUNKCJI = 10

#dekorator
def zliczanie(f):
    @wraps(f)
    def ile():
        ile.wywolan += 1
        return f()
    ile.wywolan = 0
    return ile

#funkcja wraz z przypisaniem dekoratora
@zliczanie
def funkcja():
    pass

#funkcja main():
def main():
    print('Program realizuje implementację dekoratora, który zlicza i ' \
          + 'wypisuje liczbę wywołań danej funkcji')

    #wywołanie ILE_WYWOLAN_FUNKCJI razy funkcji o nazwie funkcja
    for x in range(ILE_WYWOLAN_FUNKCJI):
        funkcja()

    print('Funkcja o nazwie %s została wykonana %d razy' \
          % (funkcja.__name__, funkcja.wywolan))
    
if __name__ == '__main__':
    main()
