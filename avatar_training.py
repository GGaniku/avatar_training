# montando as bases do programa e as informações iniciais

    # pontos iniciais das variáveis

P = O = W = F = E = A = 0

print('\033[34mTREINAMENTO AVATAR:\033[m\n')

    # montando o laço while

while True:
    Ask = str(input('Qual elemento você quer treinar agora [W, F, E, A e X para sair]? ')).upper().strip()[0]
    if Ask == 'W':
        P = int(input('Quantos pontos você treinou? '))
        W += P          # Water soma o valor dele com o valor do P
        F -= P / 2      # Fire (versão oposta) perde metade da pontuação dada no input
    elif Ask == 'F':
        P = int(input('Quantos pontos você treinou? '))
        F += P
        W -= P / 2
    elif Ask == 'E':
        P = int(input('Quantos pontos você treinou? '))
        E += P
        A -= P / 2
    elif Ask == 'A':
        P = int(input('Quantos pontos você treinou? '))
        A += P
        E -= P / 2
    elif Ask == 'X':
        break
    else:
        print('\033[31mValor inválido. Tente novamente.\033[m')
    
    # para resolver o valor negativo das pontuações:
    
    if W < 0:
        W = 0
    elif F < 0:
        F = 0
    elif E < 0:
        E = 0
    elif A < 0:
        A = 0

print(f'''\nPontuação Final:
Water: {W:.1f}
Earth: {E:.1f}
Fire: {F:.1f}
Air: {A:.1f}\n''')

# Para o código funcionar conforme o planejado, então precisa usar "and" na condição, pois assim só terá sucesso se
# TODAS as comparações forem True. Se uma não for verdade, o esquema quebra e vai para a outra condição (no else).

if (W == 0) or (F == 0) or (E == 0) or (A == 0):
    print('\033[31mRealize mais treinamentos...\033[m')
else:
    print('\033[32mTreinamento realizado com sucesso!!\033[m')
