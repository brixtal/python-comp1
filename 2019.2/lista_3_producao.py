#QUESTÃO 1

def media(a, b):
    """Esta função recebe 2 valores numéricos e retorna a média simples entre eles"""
    return (a+b)/2
def media_4_numeros (a,b,c,d):
    """Esta função recebe o valore de 4 números e retorna a média simples entre eles"""
    m1 = media (a, b)
    m2 = media (b, c)
    return media(m1,m2)

#QUESTÃO 2
def bombom(dinheiro, preco):
    """Esta função recebe o preço de um produto, o total de dinheiro que a pessoa possui e retorna a quantidade total de produtos que a pessoa pode comprar"""
    return dinheiro//preco
def troco(dinheiro, preco):
    """Esta função recebe o preço de um produto, o total de dinheiro que a pessoa possui e retorna o quanto de troco ela recebe se comprar todos os produtos que puder"""
    return dinheiro - bombom(dinheiro, preco)*preco

#QUESTÃO 3
import math
def area_circulo(raio):
    """Esta função recebe o raio de um círculo e retorna a sua área."""
    return math.pi*2*raio

#QUESTÃO 4
def numero_termos_progressoa_aritmetica(a1, an, razao):
    """Esta função recebe o primeiro termos de uma PA, o último termo de uma PA e a sua razão, retornando a quantidade de termos nessa progressão aritmética"""
    n = ((an-a1)/razao)+1
    return n
def soma_valores_progressao_aritmetica(razao, a1, an):
    return (a1+an)*numero_termos_progressoa_aritmetica(a1, an, razao)

#QUESTÃO 5
def qtd_algarismos(numero):
    """Esta função recebe um número inteiro e retorna a quantidade de algarismos neste número"""
    return len(str(numero))

#QUESTÃO 6
def valorPagamento(valor_prestacao, dias_atraso):
    """Esta função recebe o valor de uma prestação e o número de dias de atraso, e retorna quanto uma pessoa terá que pagar em função do número de dias atrasados."""
    return valor_prestacao*1.03 + vp*0.001*dias_atraso

#QUESTÃO 7
def somaImposto (custo, imposto):
    """Esta função recebe o valor do custo de um produto e o imposto para vendê-lo, retornando o preço final com o imposto incluso"""
    preco = custo*(imposto/100)+custo
    return preco

#QUESTÃO 8

def bolos (farinha,ovo,leite):
    """Esta função recebe a quantidade de farinha, ovos e leite, e retorna quantos bolos é possível fazer de acordo com a receita"""
    bolos_farinha = farinha//2
    bolos_ovos = ovo//3
    bolos_leite = leite//5
    return min (bolos_farinha,bolos_ovos,bolos_leite)
