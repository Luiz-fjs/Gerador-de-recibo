from PySimpleGUI import PySimpleGUI as sg
from os import write


usuarios = []
with open('info_recibo.txt', 'r+', encoding='Utf-8', newline='') as arquivo:
    for linha in arquivo:
        linha = linha.strip(",")
        usuarios.append(linha.split())

    for usuario in usuarios:
        nome_pai = usuario[0]
        cpf_pai = usuario[1]
        nome_crianca = usuario[2]
        cpf_crianca = usuario[3]

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('O que deseja fazer?')],
    [sg.Button('1- Fazer recibos')],
    [sg.Button('2- Adicionar criança')],
    [sg.Button('3- Mostrar lista de crianças')],
    [sg.Button('4- Remover criança')]
]

Fazer = [
    [sg.Text('Quantos dias a criança veio a terepia?')],
    #[sg.Input(key='presenca')],
    [sg.Button('OK', key='do')]
]

Adicionar = [
    [sg.Text('Nome do responsável:'), sg.Input(key='nomepai')],
    [sg.Text('CPF do responsável:'), sg.Input(key='cpfpai')],
    [sg.Text('Nome da criaça:'), sg.Input(key='nomecrianca')],
    [sg.Text('CPF da criança:'), sg.Input(key='cpfcrianca')],
    [sg.Text('Valor'), sg.Input(key='valor')],
    [sg.Button('OK', key='add')]
]

Mostrar = [
    [sg.Output(size=(30,20))]
]

Retirar = [
    [sg.Text('Qual o numero da criança que será retirada?')],
    [sg.Input(key='reitirar_num')],
    [sg.Button('OK', key='pop')]
]

#Janela
janela_menu = sg.Window('Menu',layout, )
janela_adicionar = sg.Window('Adicionar criança',Adicionar )
janela_mostrar= sg.Window('Mostrar lista de crianças',Mostrar)
janela_retirar = sg.Window('Remover criança',Retirar)

#ler ação
while True:
    eventos, valores = janela_menu.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == '2- Adicionar criança':
        janela_adicionar.read()


    if eventos == '3- Mostrar lista de crianças':
        eventos3 = janela_mostrar.read()
        print ('cpf_crianca')
        
        if eventos3 == sg.WINDOW_CLOSED:
            break




    if eventos == '4- Remover criança':
        eventos4, valores4 = janela_retirar.read()
        if eventos4 == sg.WINDOW_CLOSED:
            break
        #if eventos4 == 'pop'