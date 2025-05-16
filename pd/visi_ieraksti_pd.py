import sqlite3
DB = 'kross.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()
cursor.execute('''
    SELECT id, vards, vecums, laiks FROM rezultati
    ORDER BY laiks DESC
''')
ieraksti = cursor.fetchall()
conn.close()
if ieraksti:
    print('DB visi ieraksti')
    for id_, vards, vecums, laiks in ieraksti:
        print(f'{id_}   {vards} {vecums} - {laiks}')
else:
    print('Nav laika.')
    