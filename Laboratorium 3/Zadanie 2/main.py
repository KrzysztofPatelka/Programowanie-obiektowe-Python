#!/usr/bin/python3

from stack import Stack
import random

# Autor: Krzysztof Patelka
# Numer albumu: 117372
# Przedmiot: Języki obiektowe 1 (Python)
# Laboratorium nr 3 zadanie nr 2

# Deklaracja stałych
ILE_NA_STOS = 5

# Definicja nowej klasy Stack2, która dziedziczy po klasie Stack
class Stack2(Stack):
    def __init__(self):
        super().__init__()

    def minimum(self):
        list = []
        while not super().is_empty():
            list.append(super().top())
            super().pop()
        for el in list:
            super().push(el)
        return min(list)


# Funkcja main:
def main():
    stack = Stack2()

    # Losowanie liczb i umieszczanie ich na stosie
    for x in range(ILE_NA_STOS):
        stack.push(random.randrange(1, 100))

    print("Program losuje %d liczb i umieszcza je na stosie." \
          % ILE_NA_STOS)
    print("Rozmiar stosu: %d" % (stack.size()))
    print("Minimalna liczba na stosie: %d" % (stack.minimum()))
    print("Liczby na stosie:")

    # Wyświetlenie liczb znajdujących się na stocie i usunięcie ich z stosu
    while not stack.is_empty():
        print(stack.top(), end=", ")
        stack.pop()


if __name__ == "__main__":
    main()
