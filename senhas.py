from random import choice
import PySimpleGUI as sg

lnum = "1234567890" #lista de numeros
lsimb = "!@#$%&." #lista de simbolos
llet = "abcdefghijklmnopqrstuvwxyz" #alfabeto

#layout
sg.theme('dark')
layout = [
    [sg.Text('Caracteres:'), sg.Input(key='caracteres', size=(6, 0))],
    [sg.Text('Sua senha terá:')],
    [sg.Checkbox('Numeros', key='num'), sg.Checkbox('letras', key='letras'), sg.Checkbox('simbolos', key='simb')],
    [sg.Button('gerar senha', key='botao')],
    [sg.Output(size=(40, 7))]
]

#janela
janela = sg.Window('Gerador de senhas', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'botao':
        try:
            senha = "" #o resultado que será devolvido
            tam = int(valores['caracteres'])
            if tam == 0:
                print('Para gerar sua senha é necessário escolher o tamanho dela.')
            listas = [] #conteudo para gerar a senha
            if valores['num'] == True:
                listas += lnum
            if valores['simb'] == True:
                listas += lsimb
            if valores['letras'] == True:
                listas += llet
            if valores['num'] == False and valores['simb'] == False and valores['letras'] == False:
                print('Marque pelo menos uma checkbox')
            else:
                try:
                    for c in range(0, tam):
                        letra = choice(listas)
                        senha += letra
                    print(f"A senha que geramos foi essa: {senha}") #finalmete temos nossa senha pronta
                except:
                    print('Houve um erro na hora de gerarmos sua senha.')
        except:
            print('Ocorreu um erro inesperado.')
# usar o tratamento de excessões para gerar mensagens diferentes para o usuário
