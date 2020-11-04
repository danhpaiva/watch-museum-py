import random


def enviarTemperatura():
    temperatura = random.randrange(0, 40)
    return temperatura


def enviarUmidade():
    umidade = random.randrange(0, 100)
    return umidade
