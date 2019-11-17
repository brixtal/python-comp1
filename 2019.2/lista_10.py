#questao1
def telefones(nome):
    lista_telefonica = ('Joao:' '2233-4455', 'Pedro:''9988-7766')
    if nome not in lista_telefonica:
        return 'Telefone não cadastrado'
    return lista_telefonica[nome]

#questao2
def sem_repeticoes(lista):
    d = {}
    for elemento in lista:
        d[elemento] = 0 #adicionando o elemento como chave de um dicionário. Chaves não são repetidas, né?
    return list(d.keys()) #retornando as chaves dicionário, que são uma lista sem repetições.

#questao3
def numeros_romanos(numero):
    UNIDADES = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
    DEZENAS = {0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX ', 9: 'XC'}
    CENTENAS = {0: '', 1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}

    if numero < 1000:
        centena = numero // 100
        dezena = (numero % 100) // 10
        unidade = (numero % 100 % 10)

    return CENTENAS[centena] + DEZENAS[dezena] + UNIDADES[unidade]

#questao4
def cria_dicionario(texto):
    dicionario = {}
    lista = str.split(texto," ")
    for palavra in lista:
        if str.lower(palavra) not in dicionario:
            dicionario [str.lower(palavra)] = 1
        else :
            dicionario [str.lower(palavra)] += 1
    return dicionario


#questao5
def rna(molecula):
    dicionario = {'UUU':'Phe','CUU':'Leu','UUA':'Leu','AAG':"Lisina","UCU":'Ser','UAU':'Tyr','CAA':'Gin'}
    resultado = ''
    temp = ''
    for letra in molecula:
        temp += letra
        if len(temp) == 3:
            resultado = resultado + dicionario[temp] + '-'
            temp = ''
    return resultado[:-1] #eliminando o último hífen.

#questao6
def caixa_supermercado(lista):
    supermercado = {'amaciante':4.99,'arroz':10.90,'biscoito':1.69,'cafe':6.98,'chocolate':3.79,'farinha':2.99}
    soma = 0
    for c in lista:
        if c not in supermercado:
            soma += 0
        else:
            soma += supermercado[c]
    return soma

#questao7
def questao7(relacionamentos):
    resposta = []
    for pessoa in relacionamentos.keys():
        if pessoa == relacionamentos[relacionamentos[pessoa]]:
            resposta.append((pessoa, relacionamentos[pessoa]))
            relacionamentos[pessoa] = 'Já inserido' # Atalho para não aparecer na resposta (A,B) e (B,A)
    return resposta