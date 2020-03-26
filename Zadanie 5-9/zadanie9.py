#!/usr/bin/python3

#Autor: Krzysztof Patelka
#Numer albumu: 117372
#Przedmiot: Języki obiektowe 1 (Python)
#Zadanie numer 9

#deklaracja stałych
NAZWA_PLIKU = 'plik.txt'

#funkcja main():
def main():
    print('Program zlicza wszystkie wyrazy w danym pliku oraz wypisuje ' \
          +'ich ilość')
    try:
        ilosc_wyrazow = 0
        with open(NAZWA_PLIKU, 'r', encoding='UTF-8') as plik:
            for wiersz in plik:
                for slowo in wiersz.strip(' ,.;:\n').split():
                    ilosc_wyrazow += 1
        plik.close()
        print('Plik o nazwie %s zawiera %d słów.' \
              % (NAZWA_PLIKU, ilosc_wyrazow))
    except:
        print('Wystapił błąd')
    
if __name__ == '__main__':
    main()
