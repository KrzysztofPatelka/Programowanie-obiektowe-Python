from .abstract_view import AbstractView


class ConsoleDateView(AbstractView):
    def __init__(self, name, model):
        super().__init__(name, model)

    def add_component(self, comp):
        pass

    def update(self, *args, **kwargs):
        print('Lista zapisanych studentów w bazie danych:')
        for wiersz in args[0]:
            print('ID %2d: %s %s' % (wiersz[0], wiersz[1], wiersz[2]))
        print('---')

    def show(self):
        self.model.notify()
