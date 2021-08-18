# imports
from random import choice
import PySimpleGUI as sg

#variáveis
lnum = "1234567890" #lista de numeros
lsimb = "!@#$%&." #lista de simbolos
llet = "abcdefghijklmnopqrstuvwxyz" #alfabeto

#layout janela
sg.theme('dark') #tema
layout = [
    [sg.Text('Caracteres:'), sg.Input(key='caracteres', size=(6, 0))],
    [sg.Text('Sua senha terá:')],
    [sg.Checkbox('Numeros', key='num'), sg.Checkbox('letras', key='letras'),
     sg.Checkbox('simbolos', key='simb')],
    [sg.Button('Gerar senha', key='botao')],
    [sg.Output(size=(40, 7))]
]

#janela do programa
janela = sg.Window('Gerador de senhas', layout)
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED: #caso o usuário feche a janela
        break
    if eventos == 'botao': #quando o usurário aperta no botão "gerar senha"
        try:
            senha = "" #o resultado que será devolvido ficará aqui
            tam = int(valores['caracteres'])
            listas = [] #conteudo para gerar a senha
            if valores['num'] == True:
                listas += lnum
            if valores['simb'] == True:
                listas += lsimb
            if valores['letras'] == True:
                listas += llet
            try:
                for c in range(0, tam):
                    letra = choice(listas)
                    senha += letra
                print(f"A senha que geramos foi essa: {senha}") #finalmete temos nossa senha pronta
            except IndexError:
                print('Marque pelo menos uma checkbox')
            except Exception as erro:
                print(f'Houve um erro na hora de gerarmos sua senha.\nErro: {erro.__class__}')
        except ValueError:
            print('Escolha o tamanho da sua senha.')
        except Exception as erro:
            print(f'Ocorreu um erro inesperado.\nErro: {erro.__class__}')
