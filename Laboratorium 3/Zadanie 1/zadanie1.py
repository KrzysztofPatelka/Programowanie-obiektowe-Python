#!/usr/bin/python3

#Autor: Krzysztof Patelka
#Numer albumu: 117372
#Przedmiot: Języki obiektowe 1 (Python)
#Laboratorium nr 3 zadanie nr 1

from functools import wraps

#deklaracja stałych
ILE_LICZ_WYGENEROWAC = 10

#klasa która generuje kolejne liczby Fibonacciego
class MyFib:

    #deklaracja metody init
    def __init__(self, val_max):
        self.__current_val = 0
        self.__val_a = 1
        self.__val_b = 1
        self.__val_max = val_max

    #deklaracja metody iter
    def __iter__(self):
        return self

    #deklaracja metody next
    def __next__(self):
        tmp = self.__current_val
        if self.__current_val == 0 or self.__current_val == 1:
            tmp2 = 1
        else:
            tmp2 = self.__val_a + self.__val_b
            self.__val_a = self.__val_b
            self.__val_b = tmp2
        self.__current_val += 1
        if tmp == self.__val_max:
            raise StopIteration
        return tmp2

#implementacja kalsy jako dekoratora
class MyDecorator:

    #deklaracja metody iter
    def __init__(self, f):
        self.__f = f
        self.__ile = 0

    #deklaracja metody call
    def __call__(self, *args, **kwargs):
        self.__ile += 1
        return self.__ile

#deklaracja funkcji funkcja dekorowanej dekoratorem MyDecorator
@MyDecorator
def funkcja():
    pass

def main():
    #cześć zadania 1a
    print("Część zadania 1a:")
    print("Generator liczb Fibonacciego")
    print("Program generuje %d kolejnych liczb Fibonacciego" \
          % (ILE_LICZ_WYGENEROWAC))
    fib = MyFib(ILE_LICZ_WYGENEROWAC)
    it = iter(fib)
    for el in it:
        print(el)

    #część zadania 1b
    print("")
    print("Część zadania 1b:")
    for x in range(ILE_LICZ_WYGENEROWAC):
        funkcja()
    print('Funkcja została wykonana %d razy' % (funkcja._MyDecorator__ile))

if __name__ == "__main__":
    main()
