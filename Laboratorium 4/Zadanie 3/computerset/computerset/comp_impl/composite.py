from .component import Component


class Composite(Component):
    def __init__(self, comp_id, name, price):
        super().__init__(comp_id, name, price)
        self.__component_dict = dict()

    def add_component(self, component):
        component.prefix = '{0}{1}'.format(self.prefix, component.prefix)
        for el in component.get_children():
            el.prefix = '{0}{1}'.format(component.prefix, el.prefix)
        self.__component_dict[component.id] = component

    def remove_component(self, comp_id):
        if comp_id in self.__component_dict:
            del self.__component_dict[comp_id]

    def do_operation(self):
        print('{0}{1} cena: {2}'.format(self.prefix, self.name, self.price))
        for comp in self.__component_dict.values():
            comp.do_operation()

    def get_children(self):
        return self.__component_dict.values()
