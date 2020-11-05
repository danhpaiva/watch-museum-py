import requests


def getMaximumData(maximumData, feeds, field):
    data = []
    for i in range(10):
        data.append(int(feeds[i][field]))
    maximumData = max(data)
    return maximumData


def getMinimumData(minimumData, feeds, field):
    data = []
    for i in range(10):
        data.append(int(feeds[i][field]))
    minimumData = min(data)
    return minimumData


# Requisição no broker remoto WatchMuseum
url = 'https://api.thingspeak.com/channels/1218298/feeds.json?api_key=XRQD7C1VLCSHF0DD&results=10'
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

print(getMaximumData(temp_Max_room_01, feeds, field1))
print(getMinimumData(temp_Min_room_01, feeds, field2))
print(getMaximumData(temp_Max_room_02, feeds, field3))
print(getMinimumData(temp_Min_room_02, feeds, field4))
print(getMaximumData(temp_Max_room_03, feeds, field5))
print(getMinimumData(temp_Min_room_03, feeds, field6))
