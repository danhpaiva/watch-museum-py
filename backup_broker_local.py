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


def printData(conn):
    cursor = conn.cursor()
    cursor.execute('select * from Sensores')

    for linha in cursor.fetchall():
        print(linha)


def executarInsertDataBase(indice, temperatura01, umidade01, temperatura02,
                           umidade02, temperatura03, umidade03, registro, conn):
    cursor = conn.cursor()
    cursor.execute(
        f"insert into Sensores(id, temperatura01, umidade01, temperatura02,umidade02, temperatura03, umidade03, registro) values({str(indice)}, {str(temperatura01)}, {str(umidade01)}, {str(temperatura02)}, {str(umidade02)}, {str(temperatura03)}, {str(umidade03)}, {registro})")
    conn.commit()


def alimentarBancoDados():

    indice = verification_data.verificarIndiceBanco()

    conn = connect_database.conectarBanco()

    temperatura01 = arduino01.enviarTemperatura()
    umidade01 = arduino01.enviarUmidade()
    temperatura02 = arduino02.enviarTemperatura()
    umidade02 = arduino02.enviarUmidade()
    temperatura03 = arduino03.enviarTemperatura()
    umidade03 = arduino03.enviarUmidade()
    # Variável para buscar data no sqlite
    registro = "datetime('now','localtime')"

    indice += 1
    executarInsertDataBase(indice, temperatura01, umidade01, temperatura02,
                           umidade02, temperatura03, umidade03, registro, conn)

    printData(conn)

    connect_database.fecharBanco(conn)


print('\tBackup Broker Local')

while True:
    alimentarBancoDados()
    time.sleep(60)
