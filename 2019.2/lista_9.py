#QUESTÃO 1
import random
def gera_matriz(n,m):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(m):
            num = random.randint(1,1000)
            linha.append(num)
        matriz += [linha]
    return matriz

#QUESTÃO 2
def ocorrencias_matriz(matriz,num):
    cont = 0
    for elemento in matriz:
        if elemento == num:
            cont += 1
    return cont

#QUESTÃO 3
def media_matriz(matriz):
    soma = 0
    for linha in matriz:
       for elemento in linha:
           soma += elemento
    return soma/(len(matriz)*len(matriz[0]))

#QUESTÃO 4
def matriz_transposta(matriz):
    resposta = gera_matriz(len(matriz[0]),len(matriz)) #Gerando uma matriz para salvar o resultado.
    for i in range(len(matriz)):
        for k in range(len(matriz[0])):
            resposta[k][i] = matriz[i][k]
    return resposta

#QUESTÃO 5
def opera_linha(matriz, numero, operacao):
    if operacao == 'S':
        soma = sum(matriz[numero-1])
        return soma
    if operacao == 'M':
        media = sum(matriz[numero-1])/len(matriz[numero-1])
        return media

#QUESTÃO 6
def matriz_superior(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j > i :
                soma = soma + matriz[j]
    return soma


#QUESTÃO 7
def soma_direita(matriz):
    soma = 0
    for i in range(0, len(matriz)):
        distancia = min(i, len(matriz)-i-1)
        if distancia > 0:
            for j in range(len(matriz[i])-distancia, len(matriz[i])):
                soma += matriz[i][j]
    return soma

#QUESTÃO 8
def corrida (matriz):
    melhor = [-1,999999, -1] #Lista com o melhor resultados
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            if matriz[i][j] < melhor[1]:
                melhor[0] = i # Número do corredor
                melhor[1] = matriz[i][j] # Tempo
                melhor[2] = j # Número da volta
    return tuple(melhor)