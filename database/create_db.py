import sqlite3
DB = 'dati.db'
#savienojuma izveide ar db
conn = sqlite3.connect(DB)
#kursora izveide
cursor = conn.cursor()
#pieprasījums, kas veido tabulu DB
cursor.execute('''
    CREATE TABLE IF NOT EXISTS rezultati (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               vards TEXT NOT NULL,
               uzvards TEXT NOT NULL,
               rezultats INTEGER NOT NULL
               )
''')
#saglabā izmaiņas
conn.commit()
conn.close()
print('Tabula Rezultāti izveidota')
