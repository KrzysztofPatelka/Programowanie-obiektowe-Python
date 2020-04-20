import sqlite3 as sqlite


# Klasa student wraz z metodami
class Student():

    def __init__(self, BAZA_DANYCH):
        self.BAZA_DANYCH = BAZA_DANYCH
        self.id = 0
        self.imie = ''
        self.nazwisko = ''

    def __del__(self):
        pass

    def podaj_id(self):
        self.id = input('Podaj ID studenta: ')
        self.wczytaj_imie_nazwisko()

    def podaj_imie(self):
        self.imie = input('Podaj imię nowego studenta: ')

    def podaj_nazwisko(self):
        self.nazwisko = input('Podaj nazwisko nowego studenta: ')

    def zapisz_studenta(self):
        con = sqlite.connect(self.BAZA_DANYCH)
        cur = con.cursor()
        parametry = [self.imie, self.nazwisko]
        cur.execute('INSERT INTO student (imie, nazwisko) VALUES (?, ?)', parametry)
        con.commit()
        cur.close()
        con.close()
        return True

    def wczytaj_studentow(self):
        con = sqlite.connect(self.BAZA_DANYCH)
        cur = con.cursor()
        cur.execute('SELECT id, imie, nazwisko FROM student ORDER BY id ASC')
        con.commit()
        lista = cur.fetchall()
        cur.close()
        con.close()
        return lista

    def wczytaj_imie_nazwisko(self):
        con = sqlite.connect(self.BAZA_DANYCH)
        cur = con.cursor()
        cur.execute('SELECT imie, nazwisko FROM student WHERE id = ?', self.id)
        con.commit()
        lista = cur.fetchall()
        self.imie = lista[0][0]
        self.nazwisko = lista[0][1]
        cur.close()
        con.close()

    def zapisz_ocene(self):
        con = sqlite.connect(self.BAZA_DANYCH)
        cur = con.cursor()
        ocena = input('Nowa ocena dla studenta %s %s: ' % (self.imie, self.nazwisko))
        cur.execute('INSERT INTO ocena (ids, ocena) VALUES (?, ?)', [self.id, ocena])
        con.commit()
        cur.close()
        con.close()
        return True

    def oceny_studenta(self):
        self.wczytaj_imie_nazwisko()
        con = sqlite.connect(self.BAZA_DANYCH)
        cur = con.cursor()
        cur.execute('SELECT student.imie, student.nazwisko, ocena.ocena FROM student '
                    + 'JOIN ocena ON student.id = ocena.ids WHERE student.id = ?', self.id)
        con.commit()
        lista = cur.fetchall()
        cur.close()
        con.close()
        return lista

    def srednie_oceny(self):
        con = sqlite.connect(self.BAZA_DANYCH)
        cur = con.cursor()
        cur.execute('SELECT student.imie, student.nazwisko, avg(ocena.ocena) FROM student '
                    + 'JOIN ocena on student.id = ocena.ids GROUP BY student.id')
        con.commit()
        lista = cur.fetchall()
        cur.close()
        con.close()
        return lista
