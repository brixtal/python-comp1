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

def bolos (farinha,ovo,leite):
    """Esta função recebe a quantidade de farinha, ovos e leite, e retorna quantos bolos é possível fazer de acordo com a receita"""
    bolos_farinha = farinha//2
    bolos_ovos = ovo//3
    bolos_leite = leite//5
    return min (bolos_farinha,bolos_ovos,bolos_leite)

#QUESTÃO 5
def absoluto (numero):
    """Esta função recebe um número qualquer e retorna seu valor absoluto"""
    if numero < 0 :
        return numero *(-1)
    else:
        return numero

#QUESTÃO 6
def delta(a, b, c):
    """Esta função recebe os valores para uma função de 2º grau e retorna o seu determinante (delta)"""
    return b**2 - 4 * a * c


#QUESTÃO 7
def qtd_raizes_reais_eq2grau (a, b, c):
    """Esta função recebe os valores para uma função de 2º grau e retorna a quantidade de raízes reais essa equação possui"""
    determinante = delta(a, b, c)
    palavra = "raiz"
    if determinante > 0:
        num_raizes = 2
        palavra = "raízes"
    elif determinante < 0:
        num_raizes = "nenhuma"
    else:
        num_raizes = 1
    return "A equação {}x2 + {}x + {} apresenta {} {} reais.".format(a, b, c, num_raizes, palavra)

#QUESTÃO 8
import math
def raizes_eq2grau(a,b,c):
    """Esta função recebe os valores dos coeficientes de uma equação de 2º grau e imprime na tela seus resultados."""
    determinante = delta(a, b, c)
    if(determinante < 0):
        print("Esta equação não apresenta nenhuma raiz real.")
    elif(determinante == 0):
        x1 = (-b+(math.sqrt(delta)))/(2*a)
        print("A raiz para esta equação é: {}".format(x1))
    else:
        x1 = (-b+(math.sqrt(delta)))/(2*a)
        x2 = (-b-(math.sqrt(delta)))/(2*a)
        print("As raízes para esta equação são: {} e {}".format(x1, x2))

#QUESTÃO 9
def meia_entrada(idade, carteirinha):
    if carteirinha or idade >= 65 or idade < 21:
        return True
    else:
        return False

#QUESTÃO 10
def resultado_campeonato (c ,ce,cs,fv,fe,fs):
    pontos_vit_cor = c*3
    pontos_emp_cor = ce
    pontos_cor = pontos_vit_cor + pontos_emp_cor
    pontos_vit_fla = fv *3
    pontos_emp_fla = fe
    pontos_fla = pontos_vit_fla + pontos_emp_fla
    if  pontos_cor > pontos_fla:
        return "Cormengo"
    elif pontos_cor < pontos_fla:
        return "Flaminthians"
    elif cs > fs:
        return "Cormengo"
    elif cs < fs:
        return "Flaminthians"
    else:
        return "Empate" 
