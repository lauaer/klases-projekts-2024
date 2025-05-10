import sqlite3
DB = 'dati.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()
id_dzest = int(input('Ievadi dzēšanā ierksta ID:'))
cursor.execute('SELECT * FROM rezultati WHERE id = ?', (id_dzest,))
ieraksts = cursor.fetchone()
if not ieraksts:
    print(f'Ieraksts ar ID-{id_dzest} nav atrodams.')
else:
    cursor.execute('DELETE FROM rezultati WHERE id = ?', (id_dzest))
    conn.commit()
    print(f'Ierakts ar ID-{id_dzest} tika izdzēsts.')
conn.close