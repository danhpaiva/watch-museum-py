import requests
import time

def getMaximumData(maximumData, feeds, field):
    data = []
    for i in range(48):
        data.append(int(feeds[i][field]))
    maximumData = max(data)
    return maximumData


def getMinimumData(minimumData, feeds, field):
    data = []
    for i in range(48):
        data.append(int(feeds[i][field]))
    minimumData = min(data)
    return minimumData


def makeRequest(max_temp_01, max_temp_02, max_temp_03, min_temp_01, min_temp_02, min_temp_03):
    url = 'https://api.thingspeak.com/update?api_key=PEZAFOAXMFNBB4WX'
    field1 = '&field1=' + str(max_temp_01)
    field2 = '&field2=' + str(min_temp_01)
    field3 = '&field3=' + str(max_temp_02)
    field4 = '&field4=' + str(min_temp_02)
    field5 = '&field5=' + str(max_temp_03)
    field6 = '&field6=' + str(min_temp_03)
    request = requests.get(url+field1+field2+field3+field4+field5+field6)

    if (request.status_code == 200):
        print(
            f'\nRequisição realizada com sucesso!')
    else:
        print(
            f'\nNão houve sucesso na requisição.')


# Requisição no broker remoto WatchMuseum
url = 'https://api.thingspeak.com/channels/1218298/feeds.json?api_key=XRQD7C1VLCSHF0DD&results=48'
request = requests.get(url)

# Transformando Json em um dicionário
data = request.json()
feeds = data['feeds']
# print(data)
# print(feeds[-1]['field1'])

# Variáveis para a função calculateAverege
temp_Max_room_01 = 0
temp_Min_room_01 = 0
temp_Max_room_02 = 0
temp_Min_room_02 = 0
temp_Max_room_03 = 0
temp_Min_room_03 = 0
field1 = 'field1'
field2 = 'field2'
field3 = 'field3'
field4 = 'field4'
field5 = 'field5'
field6 = 'field6'

max_temp_01 = getMaximumData(temp_Max_room_01, feeds, field1)
min_temp_01 = getMinimumData(temp_Min_room_01, feeds, field2)
max_temp_02 = getMaximumData(temp_Max_room_02, feeds, field3)
min_temp_02 = getMinimumData(temp_Min_room_02, feeds, field4)
max_temp_03 = getMaximumData(temp_Max_room_03, feeds, field5)
min_temp_03 = getMinimumData(temp_Min_room_03, feeds, field6)

while True:
    makeRequest(max_temp_01, max_temp_02, max_temp_03,
                min_temp_01, min_temp_02, min_temp_03)
    #Backup Diário
    time.sleep(86400)
