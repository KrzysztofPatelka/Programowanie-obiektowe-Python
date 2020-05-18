from controllers.console_date_controller import ConsoleDateController
from controllers.console_app import ConsoleApp
from db import start_db

# Autor: Krzysztof Patelka
# Numer albumu: 117372
# Przedmiot: Języki obiektowe 1 (Python)
# Laboratorium nr 4 zadanie nr 4

start_db('baza.db')


def main():
    controller = ConsoleDateController()
    app = ConsoleApp(controller)
    app.run_app()

if '__main__' == __name__:
    main()
