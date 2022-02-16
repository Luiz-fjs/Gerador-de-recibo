from os import write
def apagarLista():  
    with open('info_recibo.txt', 'a', encoding='Utf-8', newline='') as arquivo:
        arquivo.writelines(f'.')

def retirar_criança(pai_nome, cpfpai, criança_nome, cpfcriança, valorcobrado):  
    with open('info_recibo.txt', 'a', encoding='Utf-8', newline='') as arquivo:
        arquivo.writelines(f'{pai_nome} {cpfpai} {criança_nome} {cpfcriança} {valorcobrado}\n')

usuarios = []
numeros = [23,43,123,43]
usuarios.append(23)
print (usuarios)
