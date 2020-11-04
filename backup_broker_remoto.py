import connect_database
import verification_data
import requests
import time


def realizarRequisicao(field1, field2, field3, field4, field5, field6, field7, url):

    # Verificação do número de registro do broker remoto
    backupThingSpeak = verification_data.verificarQuantidadeBackupThingSpeak()

    # Verificação do número de registro do broker local
    databaseSQLiteLenght = verification_data.verificarIndiceBanco()

    conn = connect_database.conectarBanco()

    while backupThingSpeak <= databaseSQLiteLenght:
        valorRegistro = ''
        cursor = conn.cursor()

        cursor.execute(
            f'select * from Sensores where id={str(backupThingSpeak)}')

        for linha in cursor.fetchall():
            valorTemperatura01 = linha[1]
            valorUmidade01 = linha[2]
            valorTemperatura02 = linha[3]
            valorUmidade02 = linha[4]
            valorTemperatura03 = linha[5]
            valorUmidade03 = linha[6]
            valorRegistro = linha[7]

        r = requests.get(url + field1 + str(valorTemperatura01) + field2 + str(valorUmidade01) + field3 + str(
            valorTemperatura02) + field4 + str(valorUmidade02) + field5 + str(valorTemperatura03) + field6 + str(valorUmidade03) + field7 + valorRegistro)

        if (r.status_code == 200):
            print(
                f'\nBackup {str(backupThingSpeak)}º\nTemperatura01: {str(valorTemperatura01)}\nUmidade:{str(valorUmidade01)}\nRegistro:{valorRegistro}')
        else:
            print(
                f'\nBackup {str(backupThingSpeak)}º não houve sucesso na requisição.')

        time.sleep(20)
        backupThingSpeak += 1
    connect_database.fecharBanco(conn)


url = 'https://api.thingspeak.com/update?api_key=YEVTJPX97JIKYWSA'
field1 = '&field1='
field2 = '&field2='
field3 = '&field3='
field4 = '&field4='
field5 = '&field5='
field6 = '&field6='
field7 = '&field7='

print("\nInício do processo de backup no ThingSpeak...")

while True:
    realizarRequisicao(field1, field2, field3, field4,
                       field5, field6, field7, url)
    time.sleep(60)
