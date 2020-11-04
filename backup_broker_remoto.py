import connect_database
import verification_data
import requests
import time


def realizarRequisicao(url, temperatura, umidade, registro, sala):

    backupThingSpeak = verification_data.verificarQuantidadeBackupThingSpeak()

    databaseSQLiteLenght = verification_data.verificarIndiceBanco()

    conn = connect_database.conectarBanco()

    while backupThingSpeak <= databaseSQLiteLenght:
        valorSala = ''
        valorTemperatura = ''
        valorUmidade = ''
        valorRegistro = ''
        cursor = conn.cursor()

        cursor.execute(
            f'select * from Sensores where id={str(backupThingSpeak)}')

        for linha in cursor.fetchall():
            valorSala = linha[1]
            valorTemperatura = linha[2]
            valorUmidade = linha[3]
            valorRegistro = linha[4]

        r = requests.get(url + sala + str(valorSala) + temperatura + str(valorTemperatura) +
                         umidade + str(valorUmidade) + registro + str(valorRegistro))

        if (r.status_code == 200):
            print(
                f'\nBackup {str(backupThingSpeak)}º\nSala:{valorSala}\nTemperatura: {str(valorTemperatura)}\nUmidade:{str(valorUmidade)}\nRegistro:{str(valorRegistro)}')
        else:
            print(
                f'\nBackup {str(backupThingSpeak)}º não houve sucesso na requisição.')

        time.sleep(20)
        backupThingSpeak += 1
    connect_database.fecharBanco(conn)


url = 'https://api.thingspeak.com/update?api_key=YEVTJPX97JIKYWSA&'
sala = 'field1='
temperatura = '&field2='
umidade = '&field3='
registro = '&field7='

print("\nInício do processo de backup no ThingSpeak...")
realizarRequisicao(url, temperatura, umidade, registro, sala)
print()
