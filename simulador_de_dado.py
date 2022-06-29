#Simulador de dado
#Simular o uso de um dado, gerando um valor de 1 até 6

from random import randint
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'
        #Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],[sg.Button('sim'),sg.Button('não')]
        ]
        #criar uma janela
        #ler os valores da tela
        #fazer algo com esses valores
    def Iniciar(self):
        #criar uma janela
        self.janela = sg.Window('Simulador de Dado',layout = self.layout)
        #ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'não' or self.eventos == 'n':
                print("Fim do simulador!")
            else:
                print("Digite sim ou não!")
        except:
            print("Ocorreu um erro ao receber a sua resposta!")
    def GerarValorDoDado(self):
        print(randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()

