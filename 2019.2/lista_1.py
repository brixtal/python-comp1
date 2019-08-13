Python 3.7.3 (default, Apr  3 2019, 19:16:38) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> # QUESTÃO 1
>>> ## Para descrever um número negativo no Python, basta colocar o símbolo menos antes do número desejado
>>> -5
-5

>>> # QUESTÃO 2
>>> ## Python aceita alguns operadores duplicados, como o ** (potenciação) e // (divisão com resultado inteiro). Além disso, ele também aceita adição e subtração com qualquer quantidade de símbolos, como será apresentado abaixo
>>> 2 ++ 4 # Ele soma 2 a +4 (4 positivo)
6
>>> 2 -- 4 # Ele subtrai 2 de -4 (4 negativo)
6
>>> 2 ** 3 # 2 elevado 3
8
>>> 54 // 7 # Eu quero a parte inteira da divisão de 54 por 7
7
>>> # Mas o que acontece se a gente repetir mais do que duas vezes um operador?
>>> 54 /// 7
SyntaxError: invalid syntax
>>> 54 ////7
SyntaxError: invalid syntax
>>> 2 *** 3
SyntaxError: invalid syntax
>>> 2 **** 3
SyntaxError: invalid syntax
>>> 54 %% 7
SyntaxError: invalid syntax
>>> ### Resposta: Dá erro. O Python não consegue entender qual a operação que você quer realizar, então ele não consegue executá-la

>>> # QUESTÃO 3
>>> 3+++4
7
>>> 3---4
-1
>>> 3++++4
7
>>> 3----4
7

>>> # QUESTÃO 4
>>> "A aula de hoje" + "é prática"
'A aula de hojeé prática'
>>> ### Observe que ficou hojeé, já que eu não coloquei o espaço em branco na concatenação das Strings
>>> "Oi" * 5
'OiOiOiOiOi'
>>> "A aula de hoje" ++ "é prática"
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    "A aula de hoje" ++ "é prática"
TypeError: bad operand type for unary +: 'str'
>>> ### Observe que deu erro, ou seja, a repetição de operadores que funcionou para expressões numéricas, mas não funciona para expressões com textos
>>> "Oi" ** 5
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    "Oi" ** 5
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

>>> # QUESTÃO 5
>>> 05
SyntaxError: invalid token
>>> ### Para Python, zero à esquerda não é aceitável

>>> # QUESTÃO 6
>>> n = 42
>>> 42 = n
SyntaxError: can/t assign to literal
>>> ### Observe que a primeira atribuição funciona, porque eu tenho um valor sendo atribuído à uma variável. Já a segunda não, porque eu tenho uma variável sendo atribuída a um número. Lembre-se de que do lado esquerdo do igual (atribuição) só podemos ter uma variável válida

>>> # QUESTÃO 7
>>> X = Y = 1
>>> X
1
>>> Y
1
>>> ### Observe que o Python entende que, quando você coloca múltiplas atribuições de variáveis, na verdade você está querendo dizer que todas possuem o mesmo valor
>>> x = y = z = k = l = m = 1
>>> x
1
>>> y
1
>>> z
1
>>> k
1
>>> l
1
>>> m
1

>>> # QUESTÃO 8
>>> hora = 13
>>> minuto = 47
>>> segundo = 33

>>> # QUESTÃO 9
>>> tempo_total_segundos = hora * 3600 + minuto * 60 + segundo
>>> tempo_total_segundos
49653

>>> # QUESTÃO 10
>>> distancia = 1_000_000 # Valor arbitário que você pode escolher
>>> velocidade_media = distancia / tempo_total_segundos
>>> velocidade_media
20.139770003826555

>>> # QUESTÃO 11
>>> velocidade_media = velocidade_media * 2.23694
>>> velocidade_media #Em milha por hora
45.05145711235978


>>> # QUESTÃO 12
>>> pi = 3.14159
>>> raio = 5
>>> volume = 4 * pi * raio ** 3 / 3
>>> volume
523.5983333333332

>>> # QUESTÃO 13
>>> temperatura_celsius = 32
>>> temperatura_fahrenheit = 9 * temperatura_celsius / 5 + 32
>>> temperatura_fahrenheit
89.6

>>> # QUESTÃO 14
>>> temperatura_kelvin_celsius = -272.15
>>> tempertura_kelvin = temperatura_celsius - temperatura_kelvin_celsius
>>> tempertura_kelvin
304.15

>>> # QUESTÃO 15
>>> hora_chegada = 7
>>> minuto_chegada = 60
>>> velocidade_onibus_1 = 25
>>> distancia_onibus_1 = 15
>>> velocidade_onibus_2 = 30
>>> distancia_onibus_2 = 10
>>> tempo_espera = 15
>>> tempo_deslocamento_onibus_1 = distancia_onibus_1 / velocidade_onibus_1
>>> tempo_deslocamento_onibus_2 = distancia_onibus_2 / velocidade_onibus_2
>>> tempo_deslocamento_onibus_1
0.6
>>> tempo_deslocamento_onibus_2
0.3333333333333333
>>> tempo_total_deslocamento_minutos = tempo_deslocamento_onibus_1 * 60 + tempo_deslocamento_onibus_2 * 60 + tempo_espera
>>> tempo_total_deslocamento_minutos
71.0
>>> hora_saida = hora_chegada - tempo_total_deslocamento_minutos // 60
>>> hora_saida
6.0
>>> minuto_saida = minuto_chegada - tempo_total_deslocamento_minutos % 60
>>> minuto_saida
49.0
>>> ### A resposta para essa questão é que você precisa sair 6:49 para chegar com certeza às 8:00 no Fundão. 
