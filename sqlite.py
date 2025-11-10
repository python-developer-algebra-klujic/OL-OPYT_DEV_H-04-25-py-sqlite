"""
Primjer: korištenje sqlite3 modula u Pythonu

Cilj: prikazati osnovne korake za rad s bazom podataka koristeći standardni Python modul `sqlite3`.
Koristimo jednostavan primjer s dvjema povezanim tablicama:
- authors (autori)
- books (knjige)

Odnos između tablica je 1:N (jedan autor ima više knjiga).
"""

import sqlite3


# ---------------------------------------------------------------------
# 1. SPOJ NA BAZU PODATAKA
# ---------------------------------------------------------------------
# Ako datoteka "library.db" ne postoji, SQLite će ju automatski stvoriti.
try:
    with sqlite3.connect("library.db") as connection:
        # Objekt "cursor" koristimo za izvršavanje SQL naredbi.
        cursor = connection.cursor()

        # ---------------------------------------------------------------------
        # 2. KREIRANJE TABLICA
        # ---------------------------------------------------------------------
        # Ako tablice ne postoje, stvorit ćemo ih pomoću SQL naredbi CREATE TABLE.
        # Uvijek koristimo IF NOT EXISTS kako bi se skripta mogla pokrenuti više puta.
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors(id)
        )
        """)

        # Nakon svake promjene strukture ili podataka u bazi, pozivamo commit()
        # da bi se promjene trajno spremile u datoteku.
        # .commit() metoda je ukljucena u with statement tako da ovo nije potrebno
        # ako koristimo with. Ako ne koristimo with onda je obvezno!!!
        # connection.commit()


        # ---------------------------------------------------------------------
        # 3. UNOS (CREATE)
        # ---------------------------------------------------------------------
        # Dodajemo jednog autora i dvije njegove knjige.
        # Korištenjem "?" izbjegavamo SQL injection napade — to je placeholder.
        cursor.execute("INSERT INTO authors (name) VALUES (?)", ("George Orwell",))
        author_id = cursor.lastrowid  # dohvaćamo ID netom unesenog autora

        cursor.execute("INSERT INTO books (title, author_id) VALUES (?, ?)", ("1984", author_id))
        cursor.execute("INSERT INTO books (title, author_id) VALUES (?, ?)", ("Animal Farm", author_id))

        # connection.commit()  # spremi sve unose


        # ---------------------------------------------------------------------
        # 4. ČITANJE (READ)
        # ---------------------------------------------------------------------
        # SELECT upit dohvaća sve redove iz tablica.
        # Rezultat vraća lista tupleova (npr. [(1, 'George Orwell'), (2, 'Agatha Christie'), ...])
        print("=== AUTHORS ===")
        for row in cursor.execute("SELECT * FROM authors"):
            print(row)

        print("\n=== BOOKS ===")
        for row in cursor.execute("SELECT * FROM books"):
            print(row)


        # ---------------------------------------------------------------------
        # 5. JOIN – SPREMANJE I DOHVAT POVEZANIH PODATAKA
        # ---------------------------------------------------------------------
        # Želimo prikazati knjige zajedno s imenom autora.
        # To se radi pomoću SQL naredbe JOIN, koja spaja redove iz dviju tablica
        # na temelju stranog ključa (author_id).
        print("\n=== BOOKS WITH AUTHORS ===")
        query = """
            SELECT
                books.title,
                authors.name
            FROM books
            JOIN authors ON books.author_id = authors.id
        """
        for row in cursor.execute(query):
            print(f"Knjiga: {row[0]}  |  Autor: {row[1]}")


        # ---------------------------------------------------------------------
        # 6. AŽURIRANJE (UPDATE)
        # ---------------------------------------------------------------------
        # Promijenimo ime autora.
        cursor.execute("UPDATE authors SET name = ? WHERE id = ?",
                       ("Eric Arthur Blair (George Orwell)", author_id))
        connection.commit()

        # Provjerimo rezultat:
        print("\n=== AFTER UPDATE ===")
        for row in cursor.execute("SELECT * FROM authors"):
            print(row)


        # ---------------------------------------------------------------------
        # 7. BRISANJE (DELETE)
        # ---------------------------------------------------------------------
        # Obično nećemo brisati sve podatke u demo primjerima, ali pokazujemo sintaksu.
        cursor.execute("DELETE FROM books WHERE id = ?", (1,))
        # connection.commit()


        # ---------------------------------------------------------------------
        # 8. ZATVARANJE BAZE
        # ---------------------------------------------------------------------
        # Uvijek zatvoriti konekciju na kraju rada.
        # .close() metoda je ukljucena u with statement tako da ovo nije potrebno
        # ako koristimo with. Ako ne koristimo with onda je obvezno!!!
        # connection.close()


except Exception as ex:
    print(f"Dogodila se greska {ex}!")

# ---------------------------------------------------------------------
# KRAJ SKRIPTE
# ---------------------------------------------------------------------
