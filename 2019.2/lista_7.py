# QUESTÃO 1
def crescimento_populacao():
    populacao_A = 80000
    populacao_B = 200000
    taxa_A = 3 / 100
    taxa_B = 1.5 / 100
    anos = 0
    while populacao_A < populacao_B:
        populacao_A = populacao_A * (1 + taxa_A)
        populacao_B = populacao_B * (1 + taxa_B)
        anos = anos + 1
    return anos

# QUESTÃO 2
def crescimento_2(populacao_A, populacao_B, taxa_A, taxa_B):
    while populacao_A < populacao_B:
        populacao_A = populacao_A * (1 + taxa_A)
        populacao_B = populacao_B * (1 + taxa_B)
        anos = anos + 1
    return anos


# QUESTÃO 3
from random import randint
def qtd_vezes_dados():
    qtd_vezes = 0
    numero = randint(1, 6)
    numero2 = randint(1, 6)
    while numero != numero2:
        qtd_vezes += 1
        numero = randint(1, 6)
        numero2 = randint(1, 6)
    return qtd_vezes


# QUESTÃO 5
def num_fibonacci(num):
    soma = 0
    v1 = 0
    v2 = 1
    contador = 0
    while contador < num:
        n = v1 + v2
        soma += n
        v1 = v2
        v2 = n
    return soma


# QUESTÃO 6
def fatorial(n):
    fact = n
    while n > 1:
        fact = fact * (n - 1)
        n -= 1
    return fact

# QUESTÃO 7
def primo(num):
    contador = 2
    while contador < num :
        if num % contador == 0:
            return False
        contador += 1
    return True

# QUESTÃO 8
def quebracabecas(lista_pecas):
    contador = 1
    while contador < len(lista_pecas):
        if contador not in lista_pecas:
            return contador
        contador += 1
    return lista_pecas[contador-1]+1