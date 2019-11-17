# Questão 1
def prod_r(x, y):
    if x == 0 or y == 0:
        return 0
    else:
        return x + prod_r(x, y - 1)

# Questão 2
def mdc_recursiva(x, y):
    if x == y:
        return x
    if x > y:
        return mdc_recursiva(x - y, y)
    else:
        return mdc_recursiva(y, x)


# Questão 3
def modulo(x, y):
    if x == y:
        return 0
    elif x < y:
        return x
    elif x > y:
        return modulo(x - y, y)

# Questão 4
def agenda_telefones():
    telefones = {}
    while True:
        nome = input("Insira o nome: ")
        if nome == 'FIM':
            break
        telefone = input("Insira o telefone: ")
        telefones[nome] = telefone
    return telefones

# Questão 5
# Baseano na resposta enviada pelo aluno Sidney Laurindo
def mensagem(name):
    print("Pô, que nome maneiro, {}!. \nBem vindo ao nosso mini-quiz de conhecimentos gerais!".format(name),
          "\nAgora,vamos iniciar umas questões?")


def Q_1():
    print("---Primeira questão---\n", "Quantos dentes uma pessoa adulta possui, se não perdeu nenhum?",
          "\n (A) - 30\n (B) - 31 \n (C) - 32 \n (D) - 33")


def Q_2():
    print("---Segunda questão---\n", "Em que ano derrubaram as Torres Gêmeas (World Trade Center) nos EUA?",
          "\n (A) - 1999\n (B) - 2000 \n (C) - 2001 \n (D) - 2002")


def Q_3():
    print("---Terceira questão---\n", "De quem é a famosa frase “Penso, logo existo”?",
          "\n (A) - Platão\n (B) - Descartes  \n (C) - Aristóteles \n (D) - Galileu Galilei")


def Q_4():
    print("---Quarta questão---\n", "Qual o nome do presidente do Brasil que ficou conhecido como Jango?\n",
          "(A) -  Jânio Quadros\n (B) - Jacinto Anjos  \n (C) - Getúlio Vargas \n (D) - João Goulart")


def Q_5():
    print("---Quinta questão---\n", "Quanto tempo a luz do Sol demora para chegar à Terra?\n",
          "(A) -  4 min \n(B) - 8 min \n (C) - 6 min \n (D) - 12 min")


def fim(x):
    print("Aêeeee, rapaz! Parabéns pelo jogo. Você ficou com {}\nVolta mais aqui,viu?!".format(x))


def jogo():
    import time
    p = 0
    name = input("Fala aê, boy/girl? Belê?! Digita aí seu nome pra gente: ")
    time.sleep(1)
    mensagem(name)
    time.sleep(1)

    Q_1()
    resposta = input("Qual a sua resposta?: ")
    letra = "c"
    time.sleep(1)
    if str.lower(resposta) == letra:
        p += 1000
        time.sleep(1)
        print(
            "Sabido,você, hein?! Bom... você ganhou 1000 pycoins com essa resposta correta! Sendo assim, você tem {} pycoins".format(
                p))
    else:
        p *= 0.7
        time.sleep(1)
        print("Peninha, hein?! Bom..., você tem {} pycoins".format(p))

    Q_2()
    resposta = input("Qual a sua resposta?: ")
    letra = "c"
    if str.lower(resposta) == letra:
        p += 1000
        time.sleep(1)
        print(
            "Sabido,você, hein?! Bom... você ganhou 1000 pycoins com essa resposta correta! Sendo assim, você tem {} pycoins".format(
                p))
    else:
        p *= 0.7
        time.sleep(1)
        print("Peninha, hein?! Bom..., você tem {} pycoins".format(p))

    Q_3()
    resposta = input("Qual a sua resposta?: ")
    letra = "b"
    if str.lower(resposta) == letra:
        p += 1000
        time.sleep(1)
        print(
            "Sabido,você, hein?! Bom... você ganhou 1000 pycoins com essa resposta correta! Sendo assim, você tem {} pycoins".format(
                p))
    else:
        p *= 0.7
        time.sleep(1)
        print("Peninha, hein?! Bom..., você tem {} pycoins".format(p))

    Q_4()
    resposta = input("Qual a sua resposta?: ")
    letra = "d"
    p *= 0.7
    if str.lower(resposta) == letra:
        p += 1000
        time.sleep(1)
        print(
            "Sabido,você, hein?! Bom... você ganhou 1000 pycoins com essa resposta correta! Sendo assim, você tem {} pycoins".format(
                p))
    else:
        p *= 0.7
        time.sleep(1)
        print("Peninha, hein?! Bom..., você tem {} pycoins".format(p))

    Q_5()
    resposta = input("Qual a sua resposta?: ")
    letra = "b"
    p *= 0.7
    if str.lower(resposta) == letra:
        p += 1000
        time.sleep(1)
        print(
            "Sabido,você, hein?! Bom... você ganhou 1000 pycoins com essa resposta correta! Sendo assim, você tem {} pycoins".format(
                p))
    else:
        p *= 0.7
        time.sleep(1)
        print("Peninha, hein?! Bom..., você tem {} pycoins".format(p))
    fim(p)