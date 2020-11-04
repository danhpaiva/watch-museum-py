import sqlite3


def conectarBanco():
    # Conectando no banco
    conn = sqlite3.connect('C:/watch-museum-py/broker_local/watch_museum.db')
    return conn

def fecharBanco(conn):
    conn.close()