from .component import Component


class Leaf(Component):
    def __init__(self, comp_id, name, price):
        super().__init__(comp_id, name, price)

    def do_operation(self):
        print('{0}{1} cena: {2}'.format(self.prefix, self.name, self.price))
