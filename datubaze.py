from pathlib import Path
base_dir = Path(__file__).resolve().parent
DB_FILE = base_dir / 'dati.db'

import sqlite3

def savienot():
    DB = sqlite3.connect(DB_FILE)
    return DB.cursor()


def get_topresult():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM rezultati")
    rezultati = c.fetchall()
    conn.close()
    dati = [
        {"id": r[0], "vards": r[1], "klikski": r[2], "laiks": r[3], "datums": r[4]}
        for r in rezultati
    ]
    return dati

def pievienot(dati):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
    INSERT INTO rezultati (vards, klikski, laiks, datums)
    VALUES (?, ?, ?, ?)
    ''', (dati['vards'], dati['klikski'], dati['laiks'], dati['datums']))
    conn.commit()
    conn.close()