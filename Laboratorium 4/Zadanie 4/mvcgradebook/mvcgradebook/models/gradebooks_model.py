from .abstract_model import AbstractModel
import sqlite3 as sqlite


class StudentList(AbstractModel):
    def __init__(self):
        super().__init__()
        self.__student_list = []

    def read_student():
        con = sqlite.connect('baza.db')
        cur = con.cursor()
        cur.execute('SELECT id, imie, nazwisko FROM student ORDER BY id ASC')
        con.commit()
        lista = cur.fetchall()
        cur.close()
        con.close()
        return lista

    def modify(self, *args, **kwargs):
        self.__student_list = StudentList.read_student()
        self.notify()

    def notify(self):
        for obs in self._obs_list.values():
            obs.update(self.__student_list)
