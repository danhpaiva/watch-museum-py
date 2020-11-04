from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests

url = 'https://api.thingspeak.com/channels/1218298/feeds.json?api_key=XRQD7C1VLCSHF0DD&results=5'


r = requests.get(url)


class MySearch(GridLayout):
    def __init__(self, **kwargs):
        super(MySearch, self).__init__(**kwargs)
        self.cols = 1
        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text='Sala', font_size=25))
        self.sala = TextInput(text='0', font_size=20, multiline=True)
        self.inside.add_widget(self.sala)

        self.inside.add_widget(Label(text='Temperatura', font_size=25))
        self.temperatura = TextInput(text='0', font_size=20, multiline=True)
        self.inside.add_widget(self.temperatura)

        self.inside.add_widget(Label(text='Umidade', font_size=25))
        self.umidade = TextInput(text='0', font_size=20, multiline=True)
        self.inside.add_widget(self.umidade)

        self.inside.add_widget(Label(text='Relatório Diário', font_size=25))
        self.relatorio_diario = TextInput(text='0', font_size=20, multiline=True)
        self.inside.add_widget(self.relatorio_diario)

        self.inside.add_widget(Label(text='Média Mensal Temperatura', font_size=25))
        self.media_mensal_temp = TextInput(text='0', font_size=20, multiline=True)
        self.inside.add_widget(self.media_mensal_temp)

        self.inside.add_widget(Label(text='Média Mensal Umidade', font_size=25))
        self.media_mensal_umid = TextInput(text='0', font_size=20, multiline=True)
        self.inside.add_widget(self.media_mensal_umid)

        self.inside.add_widget(Label(text='Média Mensal Umidade', font_size=25))
        self.registro = TextInput(text='0', font_size=20, multiline=True)
        self.inside.add_widget(self.registro)

        self.add_widget(self.inside)

        self.verificar_umidade = Button(text="Verificar Umidade", font_size=50, size_hint=(.2, .5))
        self.verificar_umidade.bind(on_press=self.pressionar)
        self.add_widget(self.verificar_umidade)
        

    def pressionar(self, instance):
        # Transformando data em um dicionário
        data = r.json()
        print(data)
        feeds = data['feeds']
        print(feeds[-1]['field2'])
        self.temperatura.text = str(feeds[-1]['field1'])
        #self.umidade.text = str(feeds[-1]['field2'])
        self.umidade.text = str(arduino.verificarUmidade())


class SearchThingSpeak(App):
    def build(self):
        return MySearch()


SearchThingSpeak().run()
