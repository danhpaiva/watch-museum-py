import connect_database
import requests
import sqlite3


def verificarIndiceBanco():
    conn = connect_database.conectarBanco()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) from Sensores')
    indice = 0
    for linha in cursor.fetchall():
        indice = linha[0]
    connect_database.fecharBanco(conn)
    return indice


def verificarQuantidadeBackupThingSpeak():
    url = 'https://api.thingspeak.com/channels/1218298/feeds.json?api_key=XRQD7C1VLCSHF0DD&results=1'
    r = requests.get(url)
    data = r.json()
    channel_lenght = data['channel']['last_entry_id']
    if channel_lenght == None:
        channel_lenght = 0
    channel_lenght += 1
    return channel_lenght
