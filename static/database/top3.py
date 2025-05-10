import sqlite3
DB = 'dati.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()
cursor.execute('''
    SELECT id, vards, uzvards, rezultats FROM rezultati
    ORDER BY rezultats DESC
    LIMIT 3
''')
top3 = cursor.fetchall()
conn.close()
if top3:
    print('Top3 rezultāti:')
    for id_, vards, uzvards, rezultats in top3:
        print(f'{id_}   {vards} {uzvards} - {rezultats}')
else:
    print('Nav rezultātu.')
    