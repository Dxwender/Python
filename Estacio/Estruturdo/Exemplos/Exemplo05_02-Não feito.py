#Declara  o vetor
lista = [10,2,5,7,6,3]

#acululador da soma
soma=0
#Varre cada elemento de dentro vetor
#for i=0 ; i<6 ;i++
for num in lista :

  if(num%2==0):

    soma=soma+num

print(f'O somatorio dos elementeos pares da lista são:',soma)