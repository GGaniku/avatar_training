# arquivo para colocar todas as funções que usarei em um upgrade do programa

def menu_inicio():
    print('=' * 65)
    print('\033[34mTREINAMENTO AVATAR:\033[m')
    print('=' * 65)

W = 1
F = 5
A = 6
E = 9

lista = [W, F, A, E]

def valor_negativo():
    for  i, elemento in enumerate(lista):
        if elemento[i] < 0:
            elemento = 0
    return lista

valor_negativo()
print(lista)