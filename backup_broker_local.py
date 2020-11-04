import arduino01
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

    temperatura01 = arduino01.enviarTemperatura()
    umidade01 = arduino01.enviarUmidade()

    # comando original do sqlite3 para pegar a data e hora atual no nosso fuso
    registro01 = "datetime('now','localtime')"

    # Criação do cursor para manipular dados sql
    cursor = conn.cursor()

    # Incrementando o índice para não dar erro no banco de dados
    indice += 1
    cursor.execute(
        f"insert into Sensores (id, sala, temperatura, umidade, registro) values({str(indice)}, 1, {str(temperatura01)},{str(umidade01)},{str(registro01)})")
    conn.commit()

    cursor.execute('select * from Sensores')

    for linha in cursor.fetchall():
        print(linha)

    connect_database.fecharBanco(conn)


print('\tBackup Broker Local')

alimentarBancoDados()
