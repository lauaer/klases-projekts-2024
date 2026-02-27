import sqlite3

#izveido db ja nav
conn = sqlite3.connect('dati.db')
c = conn.cursor()

#izveido tabulu rezultātiem, labots tabula tops uz rezultati, un astlega auto...
c.execute('''
CREATE TABLE IF NOT EXISTS rezultati (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          vards TEXT NOT NULL,
          klikski INTEGER NOT NULL,
          laiks INTEGER NOT NULL,
          datums TEXT NOT NULL
          )

''')

ieraksti = [
    ("Anonīmais", 200, 500, "2020-01-01"),
    ("Anonīmais", 200, 500, "2020-01-01"),
    ("Anonīmais", 200, 500, "2020-01-01"),
    ("Anonīmais", 200, 500, "2020-01-01"),
    ("Anonīmais", 200, 500, "2020-01-01"),
    ("Anonīmais", 200, 500, "2020-01-01"),
    ("Anonīmais", 200, 500, "2020-01-01"),
    ("Anonīmais", 200, 500, "2020-01-01"),
    ("Anonīmais", 200, 500, "2020-01-01"),
    ("Anonīmais", 200, 500, "2020-01-01"),
]

c.executemany('''
INSERT INTO rezultati (vards, klikski, laiks, datums)
VALUES (?, ?, ?, ?)
''', ieraksti)

#saglabā datus, aizver konekciju
conn.commit()
conn.close()