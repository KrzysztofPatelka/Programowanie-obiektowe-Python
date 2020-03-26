#!/usr/bin/python3

#Autor: Krzysztof Patelka
#Numer albumu: 117372
#Przedmiot: Języki obiektowe 1 (Python)
#Zadanie numer 5

#deklaracja stałych
PRZEDZIAL_MAX = 70

#funkacja wyszukująca liczby pierwsze
#zwraca listę liczb pierwszych
def wyszukaj_liczby_pierwsze(lista):
    #sprawczenie czy dana liczba jest pierwsza
    #zwraca 0 gdy liczba nie jest pierwsza
    #zwraca liczbę, gdy liczba jest pierwsza
    def sprawdz_liczba(n):
        for a in range(2, n - 1, 1):
            if n % a == 0:
                return 0
        return n

    #funkcja sprawdza czy liczba jest równa 0
    #zwraca wartość False gdy liczba jest równa 0
    #zwraca wartość True gdy liczba nie jest równa 0
    def wieksze_od_zera(n):
        if n == 0:
            return False
        else:
            return True

    #zwrócenie liczb pierwszych
    return filter(wieksze_od_zera, map(sprawdz_liczba, lista))

#funkcja main():
def main():
    print("Program szuka liczb pierwszych w przedziale od 2 do %d" \
          % (PRZEDZIAL_MAX))
    print("Liczby pierwsze w przedziale od 2 do %d:" \
          % (PRZEDZIAL_MAX))
    print(list(wyszukaj_liczby_pierwsze(list(range(2, PRZEDZIAL_MAX + 1, 1)))))
    
if __name__ == "__main__":
    main()
