Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "copyright", "credits" or "license()" for more information.
>>> # QUESTÃO 1
>>> n = 42
>>> 42 = n
SyntaxError: can't assign to literal
>>> ### Observe que a primeira atribuição funciona, porque eu tenho um valor sendo atribuído à uma variável. Já a segunda não, porque eu tenho uma variável sendo atribuída a um número. Lembre-se de que do lado esquerdo do igual (atribuição) só podemos ter uma variável válida
>>> 
>>> # QUESTÃO 2
>>> hora = 13
>>> minuto = 47
>>> segundo = 33
>>> 
>>> #QUESTÃO 3
>>> tempo = 0.65
>>> tempo_segundos = 0.65 * 60
>>> print(tempo_segundos)
39.0
>>> distancia = 200.782
>>> velocidade_media = distancia/tempo_segundos
>>> print(velocidade_media)
5.14825641025641
>>> 
>>> #QUESTÃO 4
>>> vm_mph = velocidade_media * 2.23694
>>> print(vm_mph)
11.516340694358975
>>> 
>>> #QUESTÃO 5
>>> temperatura = 32.44
>>> F = ((9*temperatura)/5) + 32 #Parênteses facultativos neste cenário
>>> print(F)
90.392
>>> 
>>> # QUESTÃO 6
>>> K = -273 + temperatura
>>> print(K)
-240.56
>>> 
>>> # QUESTÃO 7
>>> hora_chegada = 7
>>> minuto_chegada = 60
>>> velocidade_onibus_1 = 25
>>> distancia_onibus_1 = 15
>>> velocidade_onibus_2 = 30
>>> distancia_onibus_2 = 10
>>> tempo_espera = 15
>>> tempo_deslocamento_onibus_1 = distancia_onibus_1 / velocidade_onibus_1
>>> tempo_deslocamento_onibus_2 = distancia_onibus_2 / velocidade_onibus_2
>>> print(tempo_deslocamento_onibus_1)
0.6
>>> print(tempo_deslocamento_onibus_2)
0.3333333333333333
>>> tempo_total_deslocamento_minutos = tempo_deslocamento_onibus_1 * 60 + tempo_deslocamento_onibus_2 * 60 + tempo_espera
>>> print(tempo_total_deslocamento_minutos)
71.0
>>> hora_saida = hora_chegada - tempo_total_deslocamento_minutos // 60
>>> print(hora_saida)
6.0
>>> minuto_saida = minuto_chegada - tempo_total_deslocamento_minutos % 60
>>> print(minuto_saida)
49.0
>>> ### A resposta para essa questão é que você precisa sair 6:49 para chegar com certeza às 8:00 no Fundão.
>>> 
>>> 
>>> #QUESTÃO 8
>>> a = 2.1
>>> b = 3.97
>>> c = 4.45
>>> p = (a + b + c) /2
>>> import math
>>> A = math.sqrt(p*(p-a)*(p-b)*(p-c))
>>> print(A)
4.167482434276116
>>> print(A/10000) #em metros quadrados
0.0004167482434276116
>>> 
>>> #QUESTÃO 9
>>> a1 = 3.62
>>> b1 = 2.84
>>> c1 = 1.61
>>> p1 = (a1 + b1 + c1) /2
>>> A1 = math.sqrt(p1*(p1-a1)*(p1-b1)*(p1-c1))
>>> a2 = 2.84
>>> b2 = 2.08
>>> c2 = 3.34
>>> p2 = (a2 + b2 + c2) /2
>>> A2 = math.sqrt(p2*(p2-a2)*(p2-b2)*(p2-c2))
>>> a3 = 2.08
>>> b3 = 5.14
>>> c3 = 4.69
>>> p3 = (a3 + b3 + c3) /2
>>> A3 = math.sqrt(p3*(p3-a3)*(p3-b3)*(p3-c3))
>>> a4 = 2.51
>>> b4 = 6.63
>>> c4 = 5.14
>>> p4 = (a4 + b4 + c4) /2
>>> A4 = math.sqrt(p4*(p4-a4)*(p4-b4)*(p4-c4))
>>> A = A1 + A2 + A3 + A4
>>> print(A/10000)
0.0015824612433788358
>>> 
>>> #QUESTÃO 10
>>> a = 1.41
>>> b = -4.72
>>> c = -5.1
>>> delta = b**2 - 4 * a * c
>>> x1 = ((-b) + math.sqrt(delta)) / (2 * a)
>>> x2 = ((-b) - math.sqrt(delta)) / (2 * a)
>>> print(x1)
4.207232767934571
>>> print(x2)
-0.8597150374381175
>>> 
>>> #QUESTÃO 11
>>> a = 7.77
>>> b = 4.68
>>> c = -5.1
>>> delta = b**2 - 4 * a * c
>>> x1 = ((-b) + math.sqrt(delta)) / (2 * a)
>>> x2 = ((-b) - math.sqrt(delta)) / (2 * a)
>>> print(x1)
0.5631720631858022
>>> print(x2)
-1.1654886655024044
>>> 
>>> 
>>> #QUESTÃO 12
>>> r1=2.6109
>>> r2=5.4906
>>> A1 = math.pi * r1**2
>>> A2 = math.pi * r2**2
>>> print(A1)
21.415605062495644
>>> print(A2)
94.70861468183692
>>> print("Resposta: " + str(A2 - A1))
Resposta: 73.29300961934128
>>> 
>>> # QUESTÃO 13
>>> alfa = math.radians(11.49)
>>> rampa = 4.25 / math.sin(alfa)
>>> print(alfa)
0.20053833105414848
>>> print(rampa)
21.335673154850042
>>> 
>>> #QUESTÃO 14
>>> alfa = math.radians(26.74)
>>> Fx = 20 * math.sin(alfa)
>>> Fy = 20 * math.cos(alfa)
>>> print(Fx)
8.998851599113998
>>> print(Fy)
17.86114973614866
>>> 
>>> #QUESTÃO 15
>>> la1 = 128
>>> la2 = 130
>>> lo = 90
>>> cos_alfa = (la1**2 + la2**2 - lo**2) / (2*la1*la2)
>>> print(cos_alfa)
0.7567307692307692
>>> angulo_rad = math.acos(cos_alfa)
>>> print(angulo_rad)
0.7124987061116195
>>> angulo_graus = math.degrees(angulo_rad)
>>> print(angulo_rad)
0.7124987061116195
>>> print(angulo_graus)
40.82316876872779
>>> 
>>> #QUESTÃO 16
>>> frase = "Hoje a aula prática de Python é sobre fatiamento de Strings"
>>> len(frase)
59
>>> #QUESTÃO 17
>>> frase[0:4]
'Hoje'
>>> #QUESTÃO 18
>>> frase[0:11]
'Hoje a aula'
>>> #QUESTÃO 19
>>> frase[-7:]
'Strings'
>>> #QUESTÃO 20
>>> frase[23:]
'Python é sobre fatiamento de Strings'
>>> #QUESTÃO 21
>>> dia = 16
>>> dia = 16
>>> mes = 8
>>> ano = 2019
>>> salario_minimo_rj = 1238.11
>>> texto = "Hoje, {}/{}/{}, o salário mínimo do estado do Rio de Janeiro é de R$ {}.".format(dia,mes,ano,salario_minimo_rj)
>>> print(texto)
Hoje, 16/8/2019, o salário mínimo do estado do Rio de Janeiro é de R$ 1238.11.
>>> 
