import sqlite3 as sqlite


# Usunięcie bazy danych i przypisanie wartości początkowych
def start_db(BAZA_DANYCH):
    con = sqlite.connect(BAZA_DANYCH)

    with con:
        cur = con.cursor()
        cur.execute('DROP TABLE IF EXISTS dzienniki')
        cur.execute('DROP TABLE IF EXISTS dziennik')
        cur.execute('DROP TABLE IF EXISTS ocena')
        cur.execute('DROP TABLE IF EXISTS student')
        cur.execute("CREATE TABLE student (id integer PRIMARY KEY AUTOINCREMENT,"
                    + " imie text NOT NULL, nazwisko text NOT NULL);")
        cur.execute("CREATE TABLE ocena (id integer PRIMARY KEY AUTOINCREMENT, ids integer NOT NULL, "
                    + "ocena integer NOT NULL, FOREIGN KEY (ids) REFERENCES student(id));")
        cur.execute("CREATE TABLE dziennik (id integer PRIMARY KEY AUTOINCREMENT, nazwa text NOT NULL);")
        cur.execute("CREATE TABLE dzienniki (id integer PRIMARY KEY AUTOINCREMENT, idd integer NOT NULL, ids NOT NULL, "
                    + "FOREIGN KEY (idd) REFERENCES dziennik(id), FOREIGN KEY (ids) REFERENCES student(id));")
        cur.execute("INSERT INTO student (imie, nazwisko) VALUES ('Adam', 'Nowak');")
        cur.execute("INSERT INTO student (imie, nazwisko) VALUES ('Stefan', 'Adamowicz');")
        cur.execute("INSERT INTO ocena (ids, ocena) VALUES (1, 4);")
        cur.execute("INSERT INTO ocena (ids, ocena) VALUES (1, 2);")
        cur.execute("INSERT INTO ocena (ids, ocena) VALUES (1, 3);")
        cur.execute("INSERT INTO ocena (ids, ocena) VALUES (2, 5);")
        cur.execute("INSERT INTO dziennik (nazwa) VALUES ('Klasa 1');")
        cur.execute("INSERT INTO dziennik (nazwa) VALUES ('Klasa 2');")
        cur.execute("INSERT INTO dzienniki (idd, ids) VALUES (1, 1);")
        cur.execute("INSERT INTO dzienniki (idd, ids) VALUES (2, 2);")
