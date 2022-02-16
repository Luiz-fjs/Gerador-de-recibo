from os import write

def Ja_tem(Nome_criança):
    usuarios = []
    try:
        with open('info_recibo.txt', 'r', encoding='Utf-8', newline='') as arquivo:
            for linha in arquivo:
                linha = linha.strip(",")
                usuarios.append(linha.split())
            
            for usuario in usuarios:
                nome_criança = usuario[2]
                
                if Nome_criança == nome_criança:
                    return True
    except FileNotFoundError:
        return False

def adicionar_criança(pai_nome, cpfpai, criança_nome, cpfcriança, valor_cobrado):  
    with open('info_recibo.txt', 'r+', encoding='Utf-8', newline='') as arquivo:
        arquivo.writelines(f'{pai_nome} {cpfpai} {criança_nome} {cpfcriança} {valor_cobrado}\n')