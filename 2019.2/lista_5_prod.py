#QUESTÃO 1
tupla = (1,2,3,4)
nova_tupla = tupla + (5,)

#QUESTÃO 2
nota_tupla_2 = nota_tupla + ("seis",)

#QUESTÃO 3
lista = [1,2,3,4]
nova_lista = lista + [5] # ou lista.append(5) ou list.append(lista, 5)

#QUESTÃO 4
def qtd_palavras(frase):
    lista_palavras = frase.split(" ")
    qtd_palavras = len(lista_palavras)
    if frase[0] == " ":
        qtd_palavras = qtd_palavras - 1
    if frase[-1] == " ":
        qtd_palavras = qtd_palavras - 1
    return qtd_palavras

#QUESTÃO 5
def subfrase(frase, letra):
    indice = frase.index(letra)
    return frase[indice+1:]

#QUESTÃO 6
def retorna_inverso(tupla):
    return tupla[9], tupla[8], tupla[7], tupla[6], tupla[5], tupla[4], tupla[3], tupla[2], tupla[1], tupla[0]

#QUESTÃO 7
def retorna_tuplas_tipos(tupla):
    tupla_str = ()
    tupla_num = ()
    if type(tupla[0]) == str :
       tupla_str = tupla_str + (tupla[0],)
    elif type(tupla[0]) == complex or type(tupla[0]) == int or type(tupla[0]) == float:
        tupla_num = tupla_num + (tupla[0],)
    else:
        pass #Não faço nada, já que o elemento na posição 0 não é nem str, complex, float ou int
    if type(tupla[1]) == str :
       tupla_str = tupla_str + (tupla[1],)
    elif type(tupla[1]) == complex or type(tupla[1]) == int or type(tupla[1]) == float:
        tupla_num = tupla_num + (tupla[1],)
    else:
        pass #Não faço nada, já que o elemento na posição 0 não é nem str, complex, float ou int
    if type(tupla[2]) == str :
       tupla_str = tupla_str + (tupla[2],)
    elif type(tupla[2]) == complex or type(tupla[2]) == int or type(tupla[2]) == float:
        tupla_num = tupla_num + (tupla[2],)
    else:
        pass #Não faço nada, já que o elemento na posição 0 não é nem str, complex, float ou int
    return tupla_str, tupla_num

#QUESTÃO 8
def mescla_listas(lista1, lista2):
    return [lista1[0]] + [lista2[0]] + [lista1[1]] + [lista2[1]] + [lista1[2]] + [lista2[2]]

#QUESTÃO 9
def palindromo(palavra):
    if(palavra[0] == palavra[4] and palavra[1] == palavra[3]):
        return True
    return False

def lista_palindromos(lista):
    resultado = ()
    if palindromo(lista[0]):
        resultado += (lista[0],)
    if palindromo(lista[1]):
        resultado += (lista[1],)
    if palindromo(lista[2]):
        resultado += (lista[2],)
    if palindromo(lista[3]):
        resultado += (lista[3],)
    if palindromo(lista[4]):
        resultado += (lista[4],)
    if palindromo(lista[5]):
        resultado += (lista[5],)
    if palindromo(lista[6]):
        resultado += (lista[6],)
    if palindromo(lista[7]):
        resultado += (lista[7],)
    if palindromo(lista[8]):
        resultado += (lista[8],)
    if palindromo(lista[9]):
        resultado += (lista[9],)
    return resultado

