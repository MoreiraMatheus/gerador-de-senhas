# imports
from random import choice
import PySimpleGUI as sg

#variáveis
lnum = "1234567890" #lista de numeros
lsimb = "!@#$%&." #lista de simbolos
llet = "abcdefghijklmnopqrstuvwxyz" #alfabeto
lLET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #alfabeto maiusculo

#layout janela
sg.theme('dark') #tema
layout = [
    [sg.Text('Caracteres:'), sg.Input(key='caracteres', size=(6, 0))],
    [sg.Text('Sua senha terá:')],
    [sg.Checkbox('Numeros', key='num'), sg.Checkbox('Simbolos', key='simb')],
    [sg.Checkbox('Letras Minúsculas.', key='letrasmin'), sg.Checkbox('Letras Maiusculas.', key='letrasmax')],
    [sg.Button('Gerar senha', key='botao')],
    [sg.Text(size=(40, 1), key='output')],
    [sg.Output(size=(40, 1))]
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
            if tam > 40:
                janela['output'].update('limite de 40 caracteres, excedido')
            else:
                listas = [] #conteudo para gerar a senha
                if valores['num'] == True:
                    listas += lnum
                if valores['simb'] == True:
                    listas += lsimb
                if valores['letrasmin'] == True:
                    listas += llet
                if valores['letrasmax'] == True:
                    listas += lLET
                try:
                    for c in range(0, tam):
                        letra = choice(listas)
                        senha += letra
                    print('A senha que geramos foi essa: ' + senha)
                except IndexError:
                    janela['output'].update('Marque pelo menos uma checkbox')
                except Exception as erro:
                    janela['output'].update(f'Houve um erro na hora de gerarmos sua senha.\nErro: {erro.__class__}')
        except ValueError:
            janela['output'].update('Escolha o tamanho da sua senha.')
        except Exception as erro:
            janela['output'].update(f'Ocorreu um erro inesperado.\nErro: {erro.__class__}')
