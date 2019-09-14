#QUESTÃO 1
def taxa_pesca(peso):
    """ Função que recebe a quantidade de peixes pescados (em kg) e retorna o valor da taxa de pesca.
        Entrada: inteiro
        Saída: float"""
    multa = 0
    VALOR_MULTA_POR_QUILO = 4
    if(peso > 50):
        multa = VALOR_MULTA_POR_QUILO * (peso - 50)
    return multa


#QUESTÃO 2
def qtd_latas_tinta(dimensao_pintada):
    """ Função que recebe a dimensão a ser pintada (em m2) e retorna o custo (em reais) para pintar esta área.
        Entrada: inteiro
        Saída: float"""
    LITROS_POR_M2 = 1/3
    QTD_LITROS_LATA = 18
    PRECO_LATA = 80
    qtd_litros_pintura = dimensao_pintada * LITROS_POR_M2
    num_latas = qtd_litros_pintura // QTD_LITROS_LATA
    if qtd_litros_pintura % QTD_LITROS_LATA != 0:
        num_latas += 1
    custo = num_latas * PRECO_LATA
    return custo


#QUESTÃO 3
def tempo_download(tamanho_arquivo, velocidade):
    """ Função que recebe o tamanho de um arquivo (em MB) e a velocidade da conexão (em Mbps), e retorna o tempo total para o download (em segundos).
        Entrada: inteiro, inteiro
        Saída: inteiro"""
    tamanho_arquivo_mb = tamanho_arquivo * 8 #convertendo de megabytes para megabits
    tempo_total = tamanho_arquivo_mb / velocidade
    return tempo_total


#QUESTÃO 4
def conversor_leet(palavra):
    """ Função que recebe uma palavra e substitui suas letras por números, seguindo o padrão do Leet.
        Entrada: String
        Saída: String"""
    return palavra.replace('o','0').replace('O', '0').replace('i', '1').replace('I', '1').replace('e', '3').replace('E', '3').replace('a', '4').replace('A', '4').replace('s', '5').replace('S', '5').replace('t', '7').replace('T', '7')


#QUESTÃO 5
def verifica_vogal(letra):
    """ Função que recebe uma letra e retorna se ela é vogal (True) ou não (False).
        Entrada: String
        Saída: String """
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        return True
    else:
        return False

#QUESTÃO 6
def carne_tabajara(lista_informacoes):
    """ Função que calcula o valor da compra de carnes no Supermercados Tabajara.
        Entrada: lista
        Saída: lista"""
    PRECO_PROMO_FILE = 4.9
    PRECO_NORMAL_FILE = 5.8
    PRECO_PROMO_ALCATRA = 5.9
    PRECO_NORMAL_ALCATRA = 6.8
    PRECO_PROMO_PICANHA = 6.9
    PRECO_NORMAL_PICANHA = 7.8
    DESCONTO_VIP = 0.05
    tipo_pagamento = "Outros"
    total_desconto = 0
    if lista_informacoes[0] > 0:
        qtd_carne = lista_informacoes[0]
        carne_selecionada = "Filé Duplo"
    elif lista_informacoes[1] > 0:
        qtd_carne = lista_informacoes[1]
        carne_selecionada = "Alcatra"
    elif lista_informacoes[2] > 0:
        qtd_carne = lista_informacoes[2]
        carne_selecionada = "Picanha"
    else:
        print("ERRO! Não foi selecionada nenhuma carne.")
        return #Interrompo o programa para ele não executar as demais operações.
    if carne_selecionada == "Filé Duplo" :
        if(qtd_carne <= 5):
            preco_total = qtd_carne * PRECO_PROMO_FILE
        else:
            preco_total = qtd_carne * PRECO_NORMAL_FILE
    elif carne_selecionada == "Alcatra":
        if (qtd_carne <= 5):
            preco_total = qtd_carne * PRECO_PROMO_ALCATRA
        else:
            preco_total = qtd_carne * PRECO_NORMAL_ALCATRA
    else: #Se não for nem Filé, nem Alcatra, só pode ser Picanha, por isso o ELSE
        if (qtd_carne <= 5):
            preco_total = qtd_carne * PRECO_PROMO_PICANHA
        else:
            preco_total = qtd_carne * PRECO_NORMAL_PICANHA
    preco_a_pagar = preco_total
    if lista_informacoes[3]: #Nesta posição há um BOOLEAN que define se o cliente é VIP ou não, por isso não preciso comparar com nada.
        preco_a_pagar = preco_total * (1-DESCONTO_VIP)
        tipo_pagamento = "Cartão Tabajara"
        total_desconto = DESCONTO_VIP

    lista_retorno = []
    lista_retorno.append(qtd_carne)
    lista_retorno.append(preco_total)
    lista_retorno.append(tipo_pagamento)
    lista_retorno.append(total_desconto)
    lista_retorno.append(preco_a_pagar)

    return lista_retorno


#QUESTÃO 7
def pintura(dimensao_pintada):
    """ Função que apresenta a melhor combinação para a pintura de uma área qualquer.
        Entrada: float
        Saída: lista"""
    LITROS_POR_M2 = 1 / 6
    QTD_LITROS_LATA = 18
    QTD_LITROS_GALAO = 3.6
    PRECO_LATA = 80
    PRECO_GALAO = 25

    qtd_litros_pintura = dimensao_pintada * LITROS_POR_M2
    num_latas = qtd_litros_pintura // QTD_LITROS_LATA
    num_galoes = qtd_litros_pintura // QTD_LITROS_GALAO

    qtd_sobra_lata = 0
    if qtd_litros_pintura % QTD_LITROS_LATA != 0:
        num_latas += 1
        qtd_sobra_lata = num_latas * QTD_LITROS_GALAO - qtd_litros_pintura

    if qtd_litros_pintura % QTD_LITROS_GALAO != 0:
        num_galoes += 1

    preco_pintura_galao = num_galoes * PRECO_GALAO
    preco_pintura_lata = num_latas * PRECO_LATA
    preco_mistura_lata_galao = 9999999999999999999
    if QTD_LITROS_LATA - qtd_sobra_lata <= 3*QTD_LITROS_GALAO :
        # Significa que a melhor solução é a mistura de latas e galões, mas precisamos saber quantos galões são necessários.
        num_galoes = QTD_LITROS_LATA - qtd_sobra_lata // QTD_LITROS_GALAO
        if QTD_LITROS_LATA - qtd_sobra_lata % QTD_LITROS_GALAO != 0:
            num_galoes += 1
        num_latas -= 1

        preco_mistura_lata_galao = num_galoes * PRECO_GALAO + num_latas * PRECO_LATA

        lista_retorno = []
    if preco_mistura_lata_galao < preco_pintura_galao and preco_mistura_lata_galao < preco_pintura_lata:
        sobra = num_galoes * QTD_LITROS_GALAO + num_latas * QTD_LITROS_LATA - qtd_litros_pintura
        lista_retorno.append(num_latas, num_galoes, sobra, preco_mistura_lata_galao)
    elif preco_pintura_lata < preco_pintura_galao:
        sobra = num_latas * QTD_LITROS_LATA - qtd_litros_pintura
        lista_retorno.append(num_latas, 0, sobra, preco_pintura_lata)
    else:
        sobra = num_galoes * QTD_LITROS_GALAO - qtd_litros_pintura
        lista_retorno.append(0, num_galoes, sobra, preco_pintura_lata)

    return lista_retorno

from math import pow
#QUESTÃO 8
def coulomb(q1, q2, d):
    """ Função que calcula a força entre partículas.
        Entrada: float, float, float
        Saída: float"""
    k = 8.98 * 10**9
    return k * (q1*q2/pow(d,2))


#QUESTÃO 9
def areaRetangulo(x,y):
    """Função que retorna a área de um retângulo, dado seus lados."""
    return x*y
from math import sqrt
def hipotenusa(cateto1, cateto2):
    """Função que calcula a hipotenusa de um triângulo retângulo"""
    return srqt(cateto1**2 + cateto2**2)

def areaTotal(a,b,c,d,e):
    """ Função que calcula a área do polígono definido no exercício."""
    area_a_b = areaRetangulo(a,b)
    area_c_d = areaRetangulo(c,d)
    area_tri_e = areaRetangulo(hipotenusa(a,d), e)
    area_triangulo = areaRetangulo(a,d) / 2

    return area_a_b + area_c_d + area_tri_e + area_triangulo


#QUESTÃO 10
def resultado_saltos(distancia):
    """ Função que recebe uma lista de distâncias de salto e retorna outra lista com o salto mais longo e mais curto, além da média da distância dos saltos.
        Entrada: lista de floats
        Saída: lista de floats"""
    media = sum(distancia) / len(distancia)

    distancia_maxima = max(distancia)
    salto_mais_longo = distancia.index(distancia_maxima)

    distancia_minima = min(distancia)
    salto_mais_curto = distancia.index(distancia_minima)

    lista_retorno = []
    lista_retorno.append(salto_mais_longo+1) # mais 1 pq o índice começa no zero.
    lista_retorno.append(salto_mais_curto+1)
    lista_retorno.append(media)
    return lista_retorno


#QUESTÃO 11
def correcao_prova(respostas, gabarito):
    """ Função que recebe um lista com a resposta de um aluno e outra lista com o gabarito, e retorna a nota do aluno.
        Entrada: lista de strings, lista de strings
        Saída: inteiro"""
    nota = 0
    if(respostas[0] == gabarito[0]):
        nota += 1
    if (respostas[1] == gabarito[1]):
        nota += 1
    if (respostas[2] == gabarito[2]):
        nota += 1
    if (respostas[3] == gabarito[3]):
        nota += 1
    if (respostas[4] == gabarito[4]):
        nota += 1
    if (respostas[5] == gabarito[5]):
        nota += 1
    if (respostas[6] == gabarito[6]):
        nota += 1
    if (respostas[7] == gabarito[7]):
        nota += 1
    if (respostas[8] == gabarito[9]):
        nota += 1
    if (respostas[0] == gabarito[0]):
        nota += 1
    return nota


#QUESTÃO 12
def data_extenso(data):
    """ Função que recebe uma data (string - DD/MM/AAAA) e retorna essa data por extenso (string)
        Entrada: String
        Saída: String"""
    dia = data[:2]
    mes = data[3:5]
    ano = data[-4:]

    mes_extenso = ""
    if(mes == "01"):
        mes_extenso = "Janeiro"
    if(mes == "02"):
        mes_extenso = "Fevereiro"
    if(mes == "03"):
        mes_extenso = "Março"
    if(mes == "04"):
        mes_extenso = "Abril"
    if(mes == "05"):
        mes_extenso = "Maio"
    if(mes == "06"):
        mes_extenso = "Junho"
    if(mes == "07"):
        mes_extenso = "Julho"
    if(mes == "08"):
        mes_extenso = "Agosto"
    if(mes == "09"):
        mes_extenso = "Setembro"
    if(mes == "10"):
        mes_extenso = "Outubro"
    if(mes == "11"):
        mes_extenso = "Novembro"
    if(mes == "12"):
        mes_extenso = "Dezembro"

    return "{} de {} de {}".format(dia, mes_extenso, ano)

#QUESTÃO 13
def reverso_numero(num):
    """ Função que recebe um número inteiro e retorna outro número inteiro formado com os algarismos invertidos em relação à entrada.
        Entrada: inteiro
        Saída: inteiro"""
    num_texto = str(num) #Transformo o número para string
    num_reverso_texto = num_texto[::-1] #Inverto a string
    num_reverso = int(num_reverso_texto) #converto a string para inteiro
    return num_reverso

#QUESTÃO 14
def hora_am_pm(hora, minuto):
    """ Função que recebe a hora e o minuto (ambos inteiros) e retorna a hora formatada no padrão AM, PM (String)
        Entrada: inteiro, inteiro
        Saída: String"""
    minuto = str(minuto) #Converto os minutos para string
    if(len(minuto) == 1): #Verifico se os minutos são menores do que 10, para exibir a hora corretamente na saída.
        minuto = "0" + minuto
    if(0 < hora <= 11):
        return "{}:{} AM".format(hora, minuto)
    elif hora == 0:
        return "{}:{} AM".format(12, minuto)
    elif hora == 12:
        return "{}:{} PM".format(12, minuto)
    else:
        return "{}:{} PM".format(hora-12, minuto)
