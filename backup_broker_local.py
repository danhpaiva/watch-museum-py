import arduino01
import arduino02
import arduino03
import connect_database
import verification_data
from datetime import datetime
import os
import random
import requests
import sqlite3
import time


def alimentarBancoDados():

    indice = verification_data.verificarIndiceBanco()

    conn = connect_database.conectarBanco()
    cursor = conn.cursor()

    temperatura01 = arduino01.enviarTemperatura()
    umidade01 = arduino01.enviarUmidade()
    registro01 = "datetime('now','localtime')"
    indice += 1
    cursor.execute(
        f"insert into Sensores (id, sala, temperatura, umidade, registro) values({str(indice)}, 1, {str(temperatura01)},{str(umidade01)},{str(registro01)})")
    conn.commit()

    temperatura02 = arduino02.enviarTemperatura()
    umidade02 = arduino02.enviarUmidade()
    registro02 = "datetime('now','localtime')"
    indice += 1
    cursor.execute(
        f"insert into Sensores (id, sala, temperatura, umidade, registro) values({str(indice)}, 2, {str(temperatura02)},{str(umidade02)},{str(registro02)})")
    conn.commit()

    temperatura03 = arduino03.enviarTemperatura()
    umidade03 = arduino03.enviarUmidade()
    registro03 = "datetime('now','localtime')"
    indice += 1
    cursor.execute(
        f"insert into Sensores (id, sala, temperatura, umidade, registro) values({str(indice)}, 3, {str(temperatura03)},{str(umidade03)},{str(registro03)})")
    conn.commit()


    cursor.execute('select * from Sensores')

    for linha in cursor.fetchall():
        print(linha)

    connect_database.fecharBanco(conn)


print('\tBackup Broker Local')

while True:
    alimentarBancoDados()
    time.sleep(10)
