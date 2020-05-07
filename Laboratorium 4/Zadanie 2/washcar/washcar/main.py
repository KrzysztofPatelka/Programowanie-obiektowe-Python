#!/usr/bin/python3

# Autor: Krzysztof Patelka
# Numer albumu: 117372
# Przedmiot: Języki obiektowe 1 (Python)
# Laboratorium nr 4 zadanie nr 2

from wash_stra.program import Program
from wash_stra.wash_abst import WashProgramStandard, WashProgramPremium


def main():
    program_car_1 = Program(WashProgramStandard())
    program_car_2 = Program(WashProgramPremium())

    program_car_1(['Karoseria węcznie', 'Koła automatycznie'])
    program_car_2(['Karoseria automatycznie', 'Koła automatycznie'])


if '__main__' == __name__:
    main()
