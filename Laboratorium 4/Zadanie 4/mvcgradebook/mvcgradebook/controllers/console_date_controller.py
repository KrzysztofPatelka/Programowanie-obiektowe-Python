from .abstract_controller import AbstractController


class ConsoleDateController(AbstractController):
    def __init__(self, model=None, view=None):
        super().__init__(model, view)

    def get_user_input(self):
        print('--MENU--')
        print('a - przeglądaj studentów')
        print('x - zakończ')
        znak = input('Wprowadź (a/x): ')
        print('----')
        if znak == 'x':
            return False
        elif znak == 'a':
            self.model.modify()
        else:
            print('Niewłaściwa wartość')
        return True
