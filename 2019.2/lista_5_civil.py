#Questão 1 
tupla = (1,2,3,4)
nova_tupla = tupla + (5,)

#Questão 2
nota_tupla_2 = nota_tupla + ("seis",)

#Questão 3
lista = [1,2,3,4]
nova_lista = lista + [5] # ou lista.append(5) ou list.append(lista, 5)

#Questão 4
nota_lista_2 = nova_lista[3:3]=[3.5] # ou nota_lista.insert(3, 3.5) ou list.insert(nota_lista, 3, 3.5)

#Questão 5
list.sort(nova_lista_2) # ou nova_lista_2.sort()
list.reverse(nova_lista_2) # ou nova_lista_2.reverse()

#Questão 6
nota_lista_2.remove(1)

#Questão 7
del nota_lista_2[2] 

#Questão 8
3 in nova_lista

#Questão 9 
def inverte_ordem_palavras(frase):
    lista_palavra = str.split(frase, " ")
    list.reverse(lista_palavra)
    frase_inversa = str.join(" ", lista_palavra)
    return frase_inversa

#Questão 10
def retorna_invertido(nomes):
    return nomes.reverse() # ou list.reverse(nomes)

#Questão 11
def alunos_media(lista_notas):
    media_alunos = sum(lista_notas) / len(lista_notas)
    lista_notas.append(media_alunos)
    lista_notas.sort()
    pos_media = lista_notas.index(media_alunos)
    lista_alunos_acima_media = lista_nostas[pos_media+1:]
    return media_alunos, len(lista_alunos_acima_media)

#Questão 12 
def colchao_novo(dim_colchao, porta_altura, porta_largura):
    dim_colchao.sort()
    if dim_colchao[0] > porta_altura :
        if dim_colchao[0] > porta_largura :
            return False
        elif dim_colchao[1] > porta_altura:
            return False
        else:
            return True
    elif dim_colchao[1] > porta_largura :
        return False
    else:
        return True
