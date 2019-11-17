#QUESTÃO 1

def verifica_ip():
    arquivo = open("ips.txt", 'r')
    validos = []
    invalidos = []
    for linha in arquivo.readlines():
        temp = linha.strip() #Limpando \n e outros caracteres não alfanuméricos
        ip = temp.split('.')
        if int(ip[0]) >= 0 and int(ip[0]) <= 255 and int(ip[1]) >= 0 and int(ip[1]) <= 255 and int(ip[2]) >= 0 and int(ip[2]) <= 255 and int(ip[3]) >= 0 and int(ip[3]) <= 255:
            validos.append(temp)
        else:
            invalidos.append(temp)
    print('[Endereços válidos:]')
    for i in validos:
        print(i)
    print('[Enderecos inválidos:}')
    for i in invalidos:
        print(i)
    arquivo.close()

#QUESTÃO 2

def converte_mb(bytes):
    return bytes / 1000000

def gestao_disco():
    arquivo = open("usuarios.txt", 'r')
    uso_disco = {}
    total = 0
    for linha in arquivo.readlines():
        nome = linha[0:15].strip()
        espaco = converte_mb(int(linha[15:].strip()))
        total += espaco
        uso_disco[nome] = espaco
    arquivo.close()

    arquivo = open("relatorio.txt", 'w')
    arquivo.write('ACME Inc.                Uso do espaço em disco pelos usuários\n')
    arquivo.write('--------------------------------------------------------------\n')
    arquivo.write('Nr.    Usuário    Espaco utilizado    % do uso\n')
    index = 1
    for usuario in uso_disco.keys():
        arquivo.write("{}    {}    {:7.2f} MB    {:5.2f}%\n".format(index, usuario, uso_disco[usuario], uso_disco[usuario]/total))
        index += 1
    arquivo.write('Espaço total ocupado: {:7.2f} MB\n'.format(total))
    arquivo.write('Espaço médio ocuapdo: {:7.2f} MB\n'.format(total/(index-1)))
    arquivo.close()

#QUESTÃO 3
def caixa_registradora():
    print("Lojas Tabajara")
    total = 0
    contador = 1
    while (True):
        valor = float(input("Produto {}: R$ ".format(contador)))
        if valor == 0:
            break
        total += valor
        contador += 1
    print("Total: R$ {:3.2f}". format(total))
    dinheiro = float(input("Dinheiro : R$ "))
    print("Troco: R$ {:3.2f}".format(dinheiro-total))

#QUESTÃO 4
def censo():
    max_peso = -1
    min_peso = 999
    min_altura = 300
    max_altura = 0
    magro = [0,0]
    gordo = [0,0]
    alto = [0,0]
    baixo = [0,0]
    soma_peso = 0
    soma_altura = 0
    qtd_clientes = 0
    while(True):
        cod = input("Insira o seu código de cliente: ")
        if cod == '0':
            break
        qtd_clientes += 1
        altura = int(input("Sua altura (em cm): "))
        soma_altura += altura
        peso = float(input("Seu peso (em kg): "))
        soma_peso += peso
        if peso > max_peso:
            max_peso = peso
            gordo[0] = cod
            gordo[1] = peso
        if peso < min_peso:
            min_peso = peso
            magro[0] = cod
            magro[1] = peso
        if altura < min_altura:
            min_altura = altura
            baixo[0] = cod
            baixo[1] = altura
        if altura > max_altura:
            max_altura = altura
            alto[0] = cod
            alto[1] = altura
    print("Mais alto: {}-{}cm".format(alto[0], alto[1]))
    print("Mais baixo: {}-{}cm".format(baixo[0], baixo[1]))
    print("Mais magro: {}-{:5.2f}kg".format(magro[0], magro[1]))
    print("Mais gordo: {}-{:5.2f}kg".format(gordo[0], gordo[1]))
    print("Média altura: {} cm".format(int(soma_altura/qtd_clientes)))
    print("Média peso: {:5.2f} kg".format(soma_peso/qtd_clientes))

#QUESTÃO 5
def salario_funcionario(ano):
    salario = 1000
    percentual = 0.015
    for i in range(1996, ano+1):
        salario = salario * (1+percentual)
        if percentual > 0.1:
            percentual = 0.005
        percentual *= 2
    return salario

#QUESTÃO 6
def grupo_numeros():
    grupo_1 = []
    grupo_2 = []
    grupo_3 = []
    grupo_4 = []
    while (True):
        num = int(input("Insira um número: "))
        if num < 0:
            break
        elif num <= 25:
            grupo_1.append(num)
        elif num <= 50:
            grupo_2.append(num)
        elif num <= 75:
            grupo_3.append(num)
        elif num <= 100:
            grupo_4.append(num)
    print("[0-25]: {}".format(len(grupo_1)))
    print("[26-50]: {}".format(len(grupo_2)))
    print("[51-75]: {}".format(len(grupo_3)))
    print("[76-100]: {}".format(len(grupo_4)))

#QUESTÃO 7
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

#QUESTÃO 8
def soma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista.pop() + soma_lista(lista)
        #OU return lista[0] + soma_lista(lista[1:])

#QUESTÃO 9
def tamanho(obj):
    tam = 0
    for i in obj:
        tam += 1
    return tam

#QUESTÃO 10
def inserir(lista, obj, posicao):
    l = []
    for i in range(0, len(lista)):
        if i == posicao:
          l.append(obj)
        l.append(lista[i])
    return l

#QUESTÃO 11
def max(obj):
    maximo = -999999999999
    for i in obj:
        if i > maximo:
            maximo = i
    return maximo

#QUESTÃO 12
def movimento_cavalo(posicao):
    pos_horizontal = posicao[0]
    pos_vertical = int(posicao[1])-1
    if pos_horizontal == 'A':
        pos_horizontal = 0
    elif pos_horizontal == 'B':
        pos_horizontal = 1
    elif pos_horizontal == 'C':
        pos_horizontal = 2
    elif pos_horizontal == 'D':
        pos_horizontal = 3
    elif pos_horizontal == 'E':
        pos_horizontal = 4
    elif pos_horizontal == 'F':
        pos_horizontal = 5
    elif pos_horizontal == 'G':
        pos_horizontal = 6
    elif pos_horizontal == 'H':
        pos_horizontal = 7
    else:
        return #Foi colocado alguma posição inválida. Não posso continuar a execução!!!
    movimentos = 3
    for i in range(0,8):
        if pos_horizontal - 1 == i or pos_horizontal + 1 == i:
            movimentos = 2
        elif pos_horizontal - 2 == i or pos_horizontal + 2 == i:
            movimentos = 1
        for j in range(0,8):
            if (pos_vertical - movimentos == j or pos_vertical + movimentos == j) and movimentos < 3:
                print("C", end='\t')
            else:
                print("0", end='\t')
        print() #para pular a linha
        movimentos = 3

#QUESTÃO 13
def jogo_matriz(matriz):
    temp = []
    for i in matriz:
        temp.append([0]*len(i))
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[0])):
            soma = 0
            nums = 0
            media = 0
            if i-1 >= 0:
                soma += matriz[i-1][j] #somo o número de cima
                nums += 1
            if j-1 >= 0:
                soma += matriz[i][j-1] #somo o número à esquerda
                nums += 1
            if nums == 2:
                media = soma/2
            elif nums ==1:
                media = soma
            else:
                media = -9999999
            if media > matriz[i][j]:
                temp[i][j] = 0
            else:
               temp[i][j] = matriz[i][j]

    for i in temp:
        for j in i:
            print(j, end="\t")
        print()



