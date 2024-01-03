#Declara  o vetor
lista = [10,2,5,7,6,3]
#Calcula o comprimento da lista
# variavel =numero de elementos da lista que são 6
n = len (lista)
#acululador da soma
soma=0
#Varre cada vetor dalista
#for i=0 ;i<[6] ;i++
for  i in range (n):
  if(lista[i]%2==0):
    soma=soma+lista[i]

print(f'O somatorio dos elementeos pares da lista são:',soma)