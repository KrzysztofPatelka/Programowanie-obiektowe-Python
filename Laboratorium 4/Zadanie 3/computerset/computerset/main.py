#!/usr/bin/python3

# Autor: Krzysztof Patelka
# Numer albumu: 117372
# Przedmiot: Języki obiektowe 1 (Python)
# Laboratorium nr 4 zadanie nr 3

from comp_impl.composite import Composite
from comp_impl.leaf import Leaf


def main():
    leaf_1 = Leaf(1, 'Zasilacz', 250)
    leaf_2 = Leaf(2, 'Pamięć RAM', 200)
    leaf_3 = Leaf(3, 'Procesor', 350)
    leaf_4 = Leaf(4, 'Karta graficzna', 150)
    leaf_5 = Leaf(5, 'Dysk SSD', 250)
    leaf_6 = Leaf(6, 'Napę DVD', 90)
    leaf_7 = Leaf(7, 'Napęd FDD', 50)

    composite_1 = Composite(1, 'Obudowa', 100)
    composite_1.add_component(leaf_1)
    composite_1.add_component(leaf_5)
    composite_1.add_component(leaf_6)
    composite_1.add_component(leaf_7)

    composite_2 = Composite(2, 'Płyta Główna', 500)
    composite_2.add_component(leaf_2)
    composite_2.add_component(leaf_3)
    composite_2.add_component(leaf_4)
    composite_1.add_component(composite_2)

    composite_1.do_operation()


if '__main__' == __name__:
    main()
