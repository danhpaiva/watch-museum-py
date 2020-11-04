import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests

url = 'https://api.thingspeak.com/channels/1218298/feeds.json?api_key=XRQD7C1VLCSHF0DD&results=1'


r = requests.get(url)


class WatchMuseum(GridLayout):
    def __init__(self, **kwargs):
        super(WatchMuseum, self).__init__(**kwargs)
        self.cols = 1
        self.inside = GridLayout()
        self.inside.cols = 2

        self.verificar_umidade = Button(
            text="Verificar Salas", font_size=50, size_hint=(.2, .5))
        self.verificar_umidade.bind(on_press=self.pressionar)
        self.add_widget(self.verificar_umidade)

        self.inside.add_widget(Label(text='Temperatura Sala 01', font_size=25))
        self.temperatura01 = TextInput(text='0', font_size=20, multiline=True)
        self.inside.add_widget(self.temperatura01)

        self.inside.add_widget(Label(text='Umidade Sala 01', font_size=25))
        self.umidade01 = TextInput(text='0', font_size=20, multiline=True)
        self.inside.add_widget(self.umidade01)

        self.inside.add_widget(Label(text='Temperatura Sala 02', font_size=25))
        self.temperatura02 = TextInput(text='0', font_size=20, multiline=True)
        self.inside.add_widget(self.temperatura02)

        self.inside.add_widget(Label(text='Umidade Sala 02', font_size=25))
        self.umidade02 = TextInput(
            text='0', font_size=20, multiline=True)
        self.inside.add_widget(self.umidade02)

        self.inside.add_widget(
            Label(text='Temperatura Sala 03', font_size=25))
        self.temperatura03 = TextInput(
            text='0', font_size=20, multiline=True)
        self.inside.add_widget(self.temperatura03)

        self.inside.add_widget(
            Label(text='Umidade Sala 03', font_size=25))
        self.umidade03 = TextInput(
            text='0', font_size=20, multiline=True)
        self.inside.add_widget(self.umidade03)

        self.inside.add_widget(
            Label(text='Registro', font_size=25))
        self.registro = TextInput(text='0', font_size=20, multiline=True)
        self.inside.add_widget(self.registro)

        self.add_widget(self.inside)

    def pressionar(self, instance):
        # Transformando data em um dicionário
        data = r.json()
        print(data)
        feeds = data['feeds']

        self.temperatura01.text = str(feeds[-1]['field1'])
        self.umidade01.text = str(feeds[-1]['field2'])
        self.temperatura02.text = str(feeds[-1]['field3'])
        self.umidade02.text = str(feeds[-1]['field4'])
        self.temperatura03.text = str(feeds[-1]['field5'])
        self.umidade03.text = str(feeds[-1]['field6'])
        self.registro.text = str(feeds[-1]['field7'])


class SearchThingSpeak(App):
    def build(self):
        return WatchMuseum()


SearchThingSpeak().run()
