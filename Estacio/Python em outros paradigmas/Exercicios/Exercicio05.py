from time import sleep
from threading import Thread
def calcular_cubo(num,tempo_espera):
    print(f'\n Cubo {num*num*num}')
    sleep(tempo_espera)
    print('Conclusao da funcao calcular_cubo')
def calcular_quadrado(num,tempo_espera):
    print(f'\n Quadrado {num * num}')
    sleep(tempo_espera)
    print('Conclusao da funcao calcular_quadrado')
t1=Thread(target=calcular_quadrado,args=(5,3))
t2=Thread(target=calcular_cubo,args=(5,2))
t1.start()
t2.start()
t1.join()
t2.join()
print("Execuçao consluida")