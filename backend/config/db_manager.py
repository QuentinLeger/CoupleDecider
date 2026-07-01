import sqlite3
from datetime import datetime


DB_PATH = "couple_decider.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS historique_compromis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date_compromis TEXT,
            theme TEXT,
            proposition_choisie TEXT,
            note_compromis REAL,
            envie_quentin TEXT,
            envie_perrine TEXT
        )
    """)

    conn.commit()
    conn.close()

def sauvegarder_compromis(theme : str,proposition : str, note : float, envie_quentin : str, envie_perrine : str):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()


    date_du_jour = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("""
              INSERT INTO historique_compromis (date_compromis, theme, proposition_choisie, note_compromis, envie_quentin,envie_perrine) VALUES (?,?,?,?,?,?)
              """, (date_du_jour,theme,proposition,note,envie_quentin,envie_perrine))

    conn.commit()
    conn.close()


def recuperer_historique_compromis():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
              SELECT date_compromis, theme, proposition_choisie,note_compromis FROM historique_compromis ORDER BY id DESC
              """)
    historique_compromis = c.fetchall()
    conn.close()
    return historique_compromis