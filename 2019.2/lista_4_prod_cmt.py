#QUESTÃO 1
def absoluto(numero):
    if numero < 0:
        return numero * -1
    else:
        return numero

#QUESTÃO 2
def delta(a, b, c):
    """Esta função recebe os valores para uma função de 2º grau e retorna o seu determinante (delta)"""
    return b**2 - 4 * a * c

#QUESTÃO 3
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


#QUESTÃO 4
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


#QUESTÃO 5
def meia_entrada(idade, carteirinha):
    if carteirinha or idade >= 65 or idade < 21:
        return True
    else:
        return False


#QUESTÃO 6
def valorPagamento(valor_prestacao, dias_atraso):
    """Esta função recebe o valor de uma prestação e o número de dias de atraso, e retorna quanto uma pessoa terá que pagar em função do número de dias atrasados."""
    if dias_atraso <= 0:
        return prestacao
    else:
        return valor_prestacao*1.03 + vp*0.001*dias_atraso

#QUESTÃO 7
def equacao(x): #retorna y de acordo com x recebido
    if 0<=x<2:
        return x
    if 2<=x<=3.5:
        return 2
    if 3.5<x<=5:
        return 3
    if x>5:
        return (x**2) - (10*x) + 28

#QUESTÃO 8
def triangulo (a,b,c):
    if a+b < c and b+c < a and a+c < b :
        return "Impossível"
    elif a == b == c :
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"

#QUESTÃO 9
def novo_salario (salario):
    if salario <= 280 :
        return salario*1.2
    if 280<salario<=700 :
        return salario*1.15
    if 700<salario<=1500 :
        return salario*1.1
    if salario>1500 :
        return salario*1.05

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

