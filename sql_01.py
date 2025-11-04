# 1. KORAK - import sqlite3 modula za rad s SQLite bazom podataka
import sqlite3

# 2. KORAK - Kreirati konekciju na bazu
conn = sqlite3.connect('data_store/pyano.db')

# 4. KORAK - Kreirati konekciju na bazu
cursor = conn.cursor()

# 5. KORAK - Izvrsimo SQL upit bilo za kreiranje ili dohvat podataka
cursor.execute('''
    CREATE TABLE IF NOT EXISTS piano
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL,
        year_of_production INTEGER NULL
    );
''')



# 6. KORAK - "Kliknuti na gumb Save", odnosno napraviti COMMIT promjena u bazu.
conn.commit()

# 3. KORAK - Zatvoriti konekciju na bazu, odnosno osloboditi resurse.
# BILJESKA - ovaj korak ide na kraj
conn.close()
