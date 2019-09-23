#Questão 1
nota_lista_2 = nova_lista[3:3]=[3.5] # ou nota_lista.insert(3, 3.5) ou list.insert(nota_lista, 3, 3.5)

#Questão 2
list.sort(nova_lista_2) # ou nova_lista_2.sort()
list.reverse(nova_lista_2) # ou nova_lista_2.reverse()

#Questão 3
nota_lista_2.remove(1)

#Questão 4
del nota_lista_2[2] 

#Questão 5
3 in nova_lista

#Questão 6
def inverte_ordem_palavras(frase):
    lista_palavra = str.split(frase, " ")
    list.reverse(lista_palavra)
    frase_inversa = str.join(" ", lista_palavra)
    return frase_inversa

#Questão 7
def retorna_invertido(nomes):
    return nomes.reverse() # ou list.reverse(nomes)

#Questão 8
def alunos_media(lista_notas):
    media_alunos = sum(lista_notas) / len(lista_notas)
    lista_notas.append(media_alunos)
    lista_notas.sort()
    pos_media = lista_notas.index(media_alunos)
    lista_alunos_acima_media = lista_nostas[pos_media+1:]
    return media_alunos, len(lista_alunos_acima_media)
