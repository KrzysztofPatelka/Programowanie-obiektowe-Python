from abc import ABC, abstractmethod


class Module(ABC):
    def __init__(self):
        super.__init__()

    @abstractmethod
    def update(self, *args, **kwargs):
        pass


class FirstModule(Module):
    def __init__(self):
        super.__init__()

    def update(self, *args, **kwargs):
        print('Pierwszy moduł został załadowany')
        if args:
            zmienna = args[0]


class SecondModule(Module):
    def __init__(self):
        super.__init__()

    def update(self, *args, **kwargs):
        print('Drugi moduł został załadowany')
        if kwargs:
            zmienne = kwargs


class ThirdModule(Module):
    def __init__(self):
        super.__init__()

    def update(self, *args, **kwargs):
        print('Trzeci moduł został załadowany')
        if kwargs:
            zmienne = kwargs


class FourthModule(Module):
    def __init__(self):
        super.__init__()

    def update(self, *args, **kwargs):
        print('Czwarty moduł został załadowany')
        if kwargs:
            zmienne = kwargs
        if args:
            zmiennab = args[0]
