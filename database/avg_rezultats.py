import sqlite3
DB = 'dati.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()
cursor.execute('SELECT AVG(rezultats) FROM rezultati')
videjais = cursor.fetchone()[0]
conn.close()
if videjais is not None:
    print(f'Vidējais rezultāts: {videjais:.2f}')
else:
    print('Nav ierakstu datubāzā.')