from abc import ABC, abstractmethod
from cv2 import imread, rotate, ROTATE_90_CLOCKWISE, imwrite, cvtColor, COLOR_BGR2GRAY, GaussianBlur, Canny, \
    findContours, RETR_EXTERNAL, CHAIN_APPROX_NONE, drawContours

class ChangeImage(ABC):
    @abstractmethod
    def __call__(self):
        pass

class Rotation90(ChangeImage):
    def __call__(self):
        img = imread('tmp_' + self.__name)
        img = rotate(img, ROTATE_90_CLOCKWISE)
        imwrite('tmp_' + self.__name, img)
        print('Obrót o 90 stopni')

    def __init__(self, name):
        self.__name = name

class Rotation180(ChangeImage):
    def __call__(self):
        img = imread('tmp_' + self.__name)
        img = rotate(img, ROTATE_90_CLOCKWISE)
        img = rotate(img, ROTATE_90_CLOCKWISE)
        imwrite('tmp_' + self.__name, img)
        print('Obrót o 180 stopni')

    def __init__(self, name):
        self.__name = name

class Blurred(ChangeImage):
    def __call__(self):
        img = imread('tmp_' + self.__name)
        img = GaussianBlur(img, (7, 7), 0)
        imwrite('tmp_' + self.__name, img)
        print('Rozmycie obrazu')

    def __init__(self, name):
        self.__name = name

class OnlyLines(ChangeImage):
    def __call__(self):
        img = imread('tmp_' + self.__name)
        img = cvtColor(img, COLOR_BGR2GRAY)
        img = Canny(img, 30, 200)
        contours, hierarchy = findContours(img, RETR_EXTERNAL, CHAIN_APPROX_NONE)
        img = drawContours(img, contours, -1, (0, 255, 0), 3)
        imwrite('tmp_' + self.__name, img)
        print('Tylko kontury / linie obrazu')

    def __init__(self, name):
        self.__name = name

class GreyScale(ChangeImage):
    def __call__(self):
        img = imread('tmp_' + self.__name)
        img = cvtColor(img, COLOR_BGR2GRAY)
        imwrite('tmp_' + self.__name, img)
        print('Skala odcieni szarości')

    def __init__(self, name):
        self.__name = name