#!/usr/bin/python3

#Autor: Krzysztof Patelka
#Numer albumu: 117372
#Przedmiot: Języki obiektowe 1 (Python)
#Zadanie numer 6

#deklaracja stałych
ILE_LICZ_WYGENEROWAC = 10

#funkcja generująca n liczb Fibonacciego
#zwraca n liczb Fibonacciego
def generator_fibonacciego(n):
    liczba1 = 1
    liczba2 = 1
    for element in range(1, n + 1, 1):
        if element == 1:
            yield 1
        elif element == 2:
            yield 1
        else:
            tmp = liczba1 + liczba2
            liczba1 = liczba2
            liczba2 = tmp
            yield tmp

#funkcja main():
def main():
    indeks_liczby = 0
    liczba1 = 0
    liczba2 = 1
    znak = ""
    print("Generator liczb Fibonacciego")
    print("Program generuje %d kolejnych liczb Fibonacciego" \
          % (ILE_LICZ_WYGENEROWAC))
    for element in generator_fibonacciego(ILE_LICZ_WYGENEROWAC):
        print(element, end=", ")
    
if __name__ == "__main__":
    main()
