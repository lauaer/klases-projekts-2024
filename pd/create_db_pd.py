import sqlite3
DB = 'kross.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS rezultati (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               vards TEXT NOT NULL,
               vecums INTEGER NOT NULL,
               laiks INTEGER NOT NULL
               )
''')
conn.commit()
conn.close()
print('Tabula Laiks izveidota')