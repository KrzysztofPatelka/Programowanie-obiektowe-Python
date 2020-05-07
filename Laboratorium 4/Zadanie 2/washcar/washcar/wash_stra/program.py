class Program:
    def __init__(self, car_program):
        self.__car_program = car_program

    def __call__(self, wash_program):
        self.__car_program.program(wash_program)
        print(wash_program)
