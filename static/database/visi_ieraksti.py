import sqlite3
DB = 'dati.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()
cursor.execute('''
    SELECT id, vards, uzvards, rezultats FROM rezultati
    ORDER BY rezultats DESC
''')
ieraksti = cursor.fetchall()
conn.close()
if ieraksti:
    print('DB visi rezultāti')
    for id_, vards, uzvards, rezultats in ieraksti:
        print(f'{id_}   {vards} {uzvards} - {rezultats}')
else:
    print('Nav rezultātu.')
    