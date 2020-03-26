#!/usr/bin/python3

#Autor: Krzysztof Patelka
#Numer albumu: 117372
#Przedmiot: Języki obiektowe 1 (Python)
#Zadanie numer 7

from functools import wraps

#dekorator funkcji
def dekorator_funkcji(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Nazwa funkcji: %s' % (funkcja.__name__))
        print('Argumenty funkcji:')
        for element in args:
            print(element)
        for klucz, wartosc in kwargs.items():
            print('{0}={1}'.format(klucz, wartosc))
        return func(*args, **kwargs)
    return wrapper

#funkcja wraz z dekoratorem
@dekorator_funkcji
def funkcja(*args, **kwargs):
    pass

#funkcja main():
def main():
    print('Implementacja dekoratora, który wypisze nazwę i argumenty ' \
          + 'wywołanej funkcji.')
    funkcja(1, 2, 3, 4, 5, a='a', b='b', c='3')
    
if __name__ == '__main__':
    main()
