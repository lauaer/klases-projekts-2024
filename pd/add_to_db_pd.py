import sqlite3
DB = 'kross.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()
dati = []
for i in range(5):
    print(f'\nIevadi {i+1}. ierakstu:')
    vards = input('Vārds: ')
    vecums = int(input('Vecums: '))
    laiks = int(input('Laiks: '))
    dati.append((vards, vecums, laiks))
cursor.executemany('''
    INSERT INTO rezultati (vards, vecums, laiks)
    VALUES (?, ?, ?)
''', dati)
conn.commit()
conn.close()
print('Tika pievinoti 5 ieraksti.')