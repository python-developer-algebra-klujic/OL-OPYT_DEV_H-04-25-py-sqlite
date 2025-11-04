import sqlite3


DB_PATH = 'data_store/pyano.db'
sql_create_table = '''
    CREATE TABLE IF NOT EXISTS piano
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL,
        year_of_production INTEGER NULL
    );
'''

try:
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_create_table)

except Exception as ex:
    print(f'Dogodila se greska {ex}!')
