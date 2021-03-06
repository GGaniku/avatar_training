**Projeto Python Treinamento Avatar:**

    O que fazer?
    - jogo que simula um treinamento de um Avatar para dominar os 4 elementos
    - 4 elementos:
            --> Earth (E)
            --> Air (A)
            --> Water (W)
            --> Fire (F)
    - Os elementos opostos são Water e Fire (W e F) e Earth e Air (E e A)

    Como funciona?
    - O usuário deve sinalizar qual elemento quer treinar dentre os 4 existentes
        - O input do elemento deve ser pela inicial do nome do elemento (ex.: E para Earth)
        - O input apenas suporta 1 elemento por vez para realizar o treinamento

    - Depois disso, em um outro input, deve-se dizer quantos pontos (P) o treinamento obteve
        - O input deve ser realizado com números inteiros, apenas

    Regras:
    - A pontuação de todos os elementos começa valendo 0
    - Ao adicionar o P para um elemento, a pontuação do elemento oposto é reduzido em P / 2 (pontos do elemento recém adicionado)
        - Ex.: Tendo 100 pontos em Water e adicionando 100 pontos em Fire, a pontuação do Water sofre - 50 pontos (pois P do Fire / 2 = 50)
    - O input para terminar o treinamento é X
    - O valor de todos os elementos deve ser positivo. Se o resultado P de algum elemento der um valor negativo, então a pontuação passa a ser 0
    - O Output do programa (após finalizado) deve apresentar a pontuação de todos os elementos com uma casa decimal (0.1)
    - Se a pontuação de cada um dos elementos for maior que zero, então deve-se imprimir "Treinamento realizado com sucesso."
    - Se não, deve-se imprimir "Realize mais treinamentos."

    Regras de estrutura:
    - Deve ter identação e comentários
    - Todos os laços devem ser implementados com o comando while
    - Não se pode usar listas, vetores, dicionários, etc.
