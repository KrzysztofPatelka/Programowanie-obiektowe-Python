#!/usr/bin/python3

# Autor: Krzysztof Patelka
# Numer albumu: 117372
# Przedmiot: Języki obiektowe 1 (Python)
# Laboratorium nr 3 zadanie nr 4

from species.image import Image
from species.change import Rotation90, Rotation180, Blurred, OnlyLines, GreyScale
from argparse import ArgumentParser
from shutil import copyfile
from cv2 import imshow, waitKey, destroyAllWindows, imread


def main():
    parser = ArgumentParser(description='Symulacja lini produkcyjnej, obróbki zdjęć.')
    parser.add_argument('--pathfile', dest='pathfile', type=str, required=True)
    args = parser.parse_args()
    copyfile(args.pathfile, 'tmp_' + args.pathfile)

    rotation_90 = Rotation90(args.pathfile)
    rotation_180 = Rotation180(args.pathfile)
    blurred = Blurred(args.pathfile)
    only_lines = OnlyLines(args.pathfile)
    grey_scale = GreyScale(args.pathfile)

    znak = 'q'
    linia = []

    print('Symulacja lini produkcyjnej. Obróbka zdjęcia.')
    print('Nazwa pliku: %s' % (args.pathfile))
    print('Nazwa nowego pliku: %s' % ('tmp_' + args.pathfile))

    while znak != 'n':
        print('Co chcesz zrobić z plikiem?')
        print('a - obrót o 90 stopni')
        print('b - obrot o 180 stopni')
        print('c - rozmycie')
        print('d - pokaż tylko linie')
        print('e - szkala odcieni szarości')
        znak = input('Co chcesz zrobic z plikiem (a/b/c/d/e): ')
        if znak == 'a':
            image = Image(args.pathfile, rotation_90)
            linia.append(image)
        elif znak == 'b':
            image = Image(args.pathfile, rotation_180)
            linia.append(image)
        elif znak == 'c':
            image = Image(args.pathfile, blurred)
            linia.append(image)
        elif znak == 'd':
            image = Image(args.pathfile, only_lines)
            linia.append(image)
        elif znak == 'e':
            image = Image(args.pathfile, grey_scale)
            linia.append(image)
        znak = input('Dodak kolejny etap? (t/n): ')

    print('Obróbka zdjęcia, kolejne etapy:')
    for el in linia:
        el.make_change()

    img = imread('tmp_' + args.pathfile)
    imshow('Gotowy plik', img)
    waitKey(0)
    destroyAllWindows()


if __name__ == '__main__':
    main()
