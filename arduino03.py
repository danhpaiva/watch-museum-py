import random


def mediaMensalTemp():
    return 1


def mediaMensalUmid():
    return 1


def relatorioDiario():
    return "Relatorio"


def enviarTemperatura():
    temperatura = random.randrange(0, 40)
    return temperatura


def enviarUmidade():
    umidade = random.randrange(0, 100)
    return umidade
