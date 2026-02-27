import sqlite3
DB = 'dati.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()
dati = []
for i in range(5):
    print(f'\nIevadi {i+1}. ierakstu:')
    vards = input('Vārds: ')
    uzvards = input('Uzvārds: ')
    rezultats = int(input('Rezultāts: '))
    dati.append((vards, uzvards, rezultats))
cursor.executemany('''
    INSERT INTO rezultati (vards, uzvards, rezultats)
    VALUES (?, ?, ?)
''', dati)
conn.commit()
conn.close()
print('Tika pievinoti 5 ieraksti.')