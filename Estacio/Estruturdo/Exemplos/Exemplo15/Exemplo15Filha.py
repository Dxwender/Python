#definicao de funcao/nome da funcao/parametro da funcao
def encontrar_minimo (lista):
#logica
    minimo= lista[0]

    for elemento in lista:

        if (elemento<minimo):

            minimo=elemento
#Retorno da funcao
        return minimo