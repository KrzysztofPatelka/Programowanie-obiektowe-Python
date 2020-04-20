class Image:
    def __init__(self, name, change_image):
        self.__name = name
        self.change_image = change_image

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def change_image(self):
        return self.__change_image

    @change_image.setter
    def change_image(self, obj):
        self.__change_image = obj

    def make_change(self):
        self.__change_image()