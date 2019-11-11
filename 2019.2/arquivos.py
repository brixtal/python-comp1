receitas = {}
def insere_receita():
    arquivo = open('receitas.txt', 'a')
    while (True):
        nome = input("Insira o nome da receita: ")
        if nome == '':
            break
        ing = input("Insira os ingredientes: ")
        arquivo.write("{}:{}\n".format(nome, ing))
        receitas[nome] = ing
    arquivo.close()

def le_receita():
    arquivo = open("receitas.txt", 'r')
    for linha in arquivo.readlines():
        print(linha)
    arquivo.close()

def atualiza_receitas():
    try:
        arquivo = open("banana.txt", 'r')
        for linha in arquivo.readlines():
            x = linha.split(':')
            receitas[x[0]] = x[1].strip()
        arquivo.close()
    except FileNotFoundError:
        print("Não achei o arquivo =(")

def div():
    n1 = input("Numero 1:")
    n2 = input("Numero 2:")
    try:
        print(int(n1)/int(n2))
    except ZeroDivisionError:
        print("Divisão por zero")
    except ValueError:
        print("Você digitou um valor inválido")
    except:
        print("Deu ruim =(")

if __name__=="__main__":
    atualiza_receitas()

