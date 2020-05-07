#!/usr/bin/python3

# Autor: Krzysztof Patelka
# Numer albumu: 117372
# Przedmiot: Języki obiektowe 1 (Python)
# Laboratorium nr 4 zadanie nr 1

from progress.progress import Progress
from progress.observer import FirstModule, SecondModule, \
    ThirdModule, FourthModule
import progressbar
import time


def main():
    progress = Progress()
    progress.add_observer(FirstModule)
    progress.add_observer(SecondModule)
    progress.add_observer(ThirdModule)
    progress.add_observer(FourthModule)

    progress.notifi(9, y=1)

    lista = progress.list_observer()
    ile = len(lista)

    with progressbar.ProgressBar(max_value=ile) as bar:
        for i in range(ile):
            time.sleep(0.5)
            bar.update(i)

if '__main__' == __name__:
    main()
