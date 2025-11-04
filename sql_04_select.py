import sqlite3


DB_PATH = 'data_store/pyano.db'
sql_select_all = '''
    SELECT * FROM piano
'''
sql_select_one = '''
    SELECT * FROM piano
    WHERE id IS (?)
'''


try:
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        # cursor.execute(sql_select_all)
        cursor.execute(sql_select_one, (1,))
        # Samo kod dohvata podataka
        # resultset = cursor.fetchall()
        resultset = cursor.fetchone()
        print(resultset)

except Exception as ex:
    print(f'Dogodila se greska {ex}!')
