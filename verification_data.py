import arduino
from datetime import datetime
import os
import random
import requests
import sqlite3
import time


def verificarIndiceBanco():
    conn = conectarBanco()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) from Sensores')
    indice = 0
    for linha in cursor.fetchall():
        indice = linha[0]
    fecharBanco(conn)
    return indice


def verificarQuantidadeBackupThingSpeak():
    url = 'https://api.thingspeak.com/channels/1211372/feeds.json?api_key=8ZPLECEO2HMX8JFV&results=1'
    r = requests.get(url)
    data = r.json()
    channel_lenght = data['channel']['last_entry_id']
    return channel_lenght
