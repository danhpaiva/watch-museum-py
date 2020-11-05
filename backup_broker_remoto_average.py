import requests

# Calcular média's no broker remoto
def calculateAverege(averege, feeds, field):
    for i in range(10):
        averege += int(feeds[i][field])
    averege /= 10
    return averege

# Requisição no broker remoto WatchMuseum
url = 'https://api.thingspeak.com/channels/1218298/feeds.json?api_key=XRQD7C1VLCSHF0DD&results=10'
request = requests.get(url)

# Transformando Json em um dicionário
data = request.json()
feeds = data['feeds']
# print(data)
# print(feeds[-1]['field1'])

#Criação de vaiáveis para a função
average_temp_room_01 = 0
average_temp_room_02 = 0
average_temp_room_03 = 0
average_humid_room_01 = 0
average_humid_room_02 = 0
average_humid_room_03 = 0
field1 = 'field1'
field2 = 'field2'
field3 = 'field3'
field4 = 'field4'
field5 = 'field5'
field6 = 'field6'

print(calculateAverege(average_temp_room_01, feeds, field1))
print(calculateAverege(average_humid_room_01, feeds, field2))
print(calculateAverege(average_temp_room_02, feeds, field3))
print(calculateAverege(average_humid_room_02, feeds, field4))
print(calculateAverege(average_temp_room_03, feeds, field5))
print(calculateAverege(average_humid_room_02, feeds, field6))

