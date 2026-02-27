import sqlite3
DB = 'dati.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()
cursor.execute('SELECT AVG(rezultats) FROM rezultati')
videjais = cursor.fetchone()[0]
cursor.execute('''
    SELECT id, vards, uzvards, rezultats FROM rezultati
    WHERE rezultats > ?
    ORDER BY rezultats DESC
''', (videjais,))
labakie = cursor.fetchall()
conn.close()
if labakie:
    print('Rezultāti virs vidējā:')
    for id_, vards, uzvards, rezultats in labakie:
        print(f'{id_}   {vards} {uzvards} - {rezultats}')
else:
    print('Nav rezultātu.')
    