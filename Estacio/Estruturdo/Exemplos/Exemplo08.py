quantidade: int= 0
nota : int
soma : int =0
media: int=0

quantidade=eval(input("Digite a quantidade de notas"))

for nota in range (quantidade) :

  print("Digite a sua nota: ", (nota + 1))
  nota=eval(input())
  if nota<1 or nota>10:
      print("Nota invalida por favor começe novamente")
      break
     # print("Digite a nota novamente: ")
      #nota = eval(input())

soma=soma+nota
media=soma/quantidade
print("A soma das notas e: ",soma)
print("A media das nostas são: ",media)