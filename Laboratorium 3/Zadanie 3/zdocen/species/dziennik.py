import sqlite3 as sqlite


# Klasa dziennik wraz z metodami
class Dziennik():

    def __init__(self, BAZA_DANYCH):
        self.BAZA_DANYCH = BAZA_DANYCH
        self.id = 0
        self.nazwa = ''

    def __del__(self):
        pass

    def dodaj_nazwe_dziennika(self):
        self.nazwa = input('Podaj nazwę nowego dziennika: ')

    def zapisz_dziennik(self):
        con = sqlite.connect(self.BAZA_DANYCH)
        cur = con.cursor()
        parametry = [self.nazwa]
        cur.execute('INSERT INTO dziennik (nazwa) VALUES (?)', parametry)
        con.commit()
        cur.close()
        con.close()
        return True

    def wczytaj_dzienniki(self):
        con = sqlite.connect(self.BAZA_DANYCH)
        cur = con.cursor()
        cur.execute('SELECT id, nazwa FROM dziennik ORDER BY id ASC;')
        con.commit()
        lista = cur.fetchall()
        cur.close()
        con.close()
        return lista