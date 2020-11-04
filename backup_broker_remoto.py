import arduino
from datetime import datetime
import os
import random
import requests
import sqlite3
import time

def realizarRequisicao(url, temperatura, umidade, data):

    backupThingSpeak = verificarQuantidadeBackupThingSpeak()

    if backupThingSpeak == None:
        backupThingSpeak = 0

    # Pegar primeiro índice válido do banco
    backupThingSpeak += 1

    databaseSQLiteLenght = verificarIndiceBanco()

    conn = conectarBanco()

    while backupThingSpeak <= databaseSQLiteLenght:
        valor = ''
        valor2 = ''
        valor3 = ''
        cursor = conn.cursor()

        cursor.execute(
            f'select * from Sensores where id={str(backupThingSpeak)}')

        for linha in cursor.fetchall():
            valor = linha[1]
            valor2 = linha[2]
            valor3 = linha[3]

        r = requests.get(url + temperatura + str(valor) +
                         umidade + str(valor2) + data + str(valor3))

        if (r.status_code == 200):
            print(
                f'\nBackup {str(backupThingSpeak)}º\nTemperatura: {str(valor)}\nUmidade:{str(valor2)}\nData:{str(valor3)}')
        else:
            print(
                f'\nBackup {str(backupThingSpeak)}º não houve sucesso na requisição.')

        time.sleep(20)
        backupThingSpeak += 1
    fecharBanco(conn)

os.system('cls')

url = 'https://api.thingspeak.com/update?api_key=Z4CXNR24JO3PNN4L&'
temperatura = 'field1='
umidade = '&field2='
data = '&field3='

print("\nInício do processo de backup no ThingSpeak...")
realizarRequisicao(url, temperatura, umidade, data)
print()