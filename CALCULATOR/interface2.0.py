from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label

class WindowManager(ScreenManager):

    pass

class insert(Screen):
    
    def __init__(self, **kwargs):

        super(insert, self).__init__(**kwargs)

        self.investimentos = []
        self.totalinvests = []
        self.rendimentos = []
        self.rendmenss = []

        self.aportetot = 0
        self.investimentotot = 0
        self.rendimentotot = 0
        self.rendmenstot = 0
        self.totalinvesttot = 0


        mainlayout = BoxLayout(orientation = 'vertical', spacing=10, padding=10)
        buttonslayout = BoxLayout(size_hint = (1, 1.5), spacing=10)

        self.aporte_input = TextInput(multiline = False,
         hint_text = "Valor do aporte mensal", font_size = 20)
        self.juros_input  = TextInput(multiline = False,
         hint_text = "Valor da taxa de juros", font_size = 20)
        self.tempo_input  = TextInput(multiline = False,
         hint_text = "Tempo de investimento em meses", font_size = 20)
        
        mainlayout.add_widget(self.aporte_input)
        mainlayout.add_widget(self.tempo_input)
        mainlayout.add_widget(self.juros_input)

        button1 = Button(text = 'CALCULAR',
                          pos_hint = {'center_x': .1, 'center_y': .5}, size_hint = (0.2, 1))
        
        button2 = Button(text = 'SAIR',
                          pos_hint = {'center_x': .3, 'center_y': .5}, size_hint = (0.2, 1))
        
        button3 = Button(text = 'CONTINUAR',
                          pos_hint = {'center_x': .5, 'center_y': .5}, size_hint = (0.2, 1))
        
        button4 = Button(text = 'ENCERRAR',
                          pos_hint = {'center_x': .7, 'center_y': .5}, size_hint = (0.2, 1))
        
        self.resultado = TextInput(multiline = True, readonly = True, font_size = 18)

        button1.bind(on_press = self.on_button_press)
        button2.bind(on_press = self.on_button_press)
        button3.bind(on_press = self.on_button_press)
        button4.bind(on_press = self.on_button_press)

        buttonslayout.add_widget(button1)
        buttonslayout.add_widget(button2)
        buttonslayout.add_widget(button3)
        buttonslayout.add_widget(button4)

        mainlayout.add_widget(self.resultado)
        mainlayout.add_widget(buttonslayout)

        self.add_widget(mainlayout)

    def on_button_press(self, instance):

        if instance.text == 'SAIR':

            self.manager.transition.direction = 'up'
            self.manager.current = 'result'
        
        elif instance.text == 'CALCULAR':
    
            self.calculator()
        
        elif instance.text == 'CONTINUAR':

            self.aporte_input.text = ''
            self.tempo_input.text = ''
            self.juros_input.text = ''
        
        elif instance.text == 'ENCERRAR':

            App.get_running_app().stop()


    def calculator(self):

        aporte = float(self.aporte_input.text)
        juros = float(self.juros_input.text)/100
        tempo =int(self.tempo_input.text)

        investimento = aporte * (1 + juros) * (((1 + juros)**tempo - 1) / juros)
        totalinvest = tempo*aporte
        rendimento = investimento - totalinvest
        rendmens = (aporte*juros)

        aporte = aporte*tempo
        self.investimentos.append(investimento)
        self.totalinvests.append(totalinvest)
        self.rendimentos.append(rendimento)
        self.rendmenss.append(rendmens)

        self.investimentotot = sum(self.investimentos)
        self.rendimentotot = sum(self.rendimentos)
        self.rendmenstot =sum(self.rendmenss)
        self.totalinvesttot = sum(self.totalinvests)

        self.resultado.text =(
        f"\nO rendimento foi de R${rendimento:.2f}"
        f"\nO total investido foi de R${aporte:.2f}"
        f"\nO total existente é de R${investimento:.2f}\n"
        f"O rendimento mensal a partir do último mês será de R${rendmens:.2f}\n"
        )
    
    def get_results(self):

        return self.investimentotot, self.rendimentotot, self.rendmenstot, self.totalinvesttot
    
        
class result(Screen):
    
    def __init__(self, **kwargs):

        super(result, self).__init__(**kwargs)

        self.resultadotot = Label(font_size = 24)

        self.add_widget(self.resultadotot)

    def on_enter(self):

        insert_screen = self.manager.get_screen('insert')
        investimentotot, rendimentotot, rendmenstot, totalinvesttot = insert_screen.get_results()

        self.resultadotot.text = (
        f"\nO rendimento total foi de R${rendimentotot:.2f}"
        f"\nO total investido foi de R${totalinvesttot:.2f}"
        f"\nO total acumulado é de R${investimentotot:.2f}\n"
        f"O rendimento mensal a partir do último mês será de R${rendmenstot:.2f}\n"
        )

class MainApp(App):

    def build(self):

        sm = WindowManager()
        sm.add_widget(insert(name = 'insert'))
        sm.add_widget(result(name = 'result'))

        return sm


app = MainApp()
app.run()