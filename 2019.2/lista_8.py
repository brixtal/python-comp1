# QUESTÃO 1
def repetir():
    for x in range (2, 1901):
        print(x)

# QUESTÃO 2
def soma():
    soma=0
    for x in range(500,1201):
        soma=soma+x
    return soma

# QUESTÃO 3
def soma_impares(x):
    soma=0
    for n in range(1, x+1, 2):
        soma = soma+n
    return soma

# QUESTÃO 4
def nomes(lista, qtd_letras):
    quantidade= 0
    for y in lista:
        if len(y) > qtd_letras:
            quantidade += 1
    return quantidade

# QUESTÃO 5
from math import factorial
def soma_fatorial():
    soma= 0
    for x in range(1,11):
        soma= soma + factorial(x)
    return soma

# QUESTÃO 6
def eprimo(num):
    for x in range(2, num):
        if numero % x == 0:
            return False
        else:
            return True

#QUESTÃO 7
def somaprimo (x, y):
    soma=0
    for i in range(x, y+1):
        if eprimo(i):
            soma= soma+i
        return soma

# QUESTÃO 8
def  fatorial (Y):
    fat=1
    for x in range(1, Y+1):
        fat= fat * x
    return fat

#  QUESTÃO 9
def serie_1():
    soma= 1
    for x in range(1,51):
        soma += (2*x-1)/x
    return soma

# QUESTÃO 10
def serie_2():
    soma= 0
    for x in range(1,11):
        soma= soma + (-1)**(x+1)*(1/x**2)
    return soma

# QUESTÃO 11
def lingua_p (texto):
    vogais = ['a', 'e','i', 'o', 'u']
    palavra = ''
    for letra in texto:
        if letra in vogais:
            palavra = palavra + 'p' + letra + 'p'
        else:
            palavra = palavra + letra
    return palavra