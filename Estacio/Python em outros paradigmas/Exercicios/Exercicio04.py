from time import sleep
from threading import Thread
def tarefa (tempo_espera,nome_tarefa):
    print(f'Iiniando a tarefa {nome_tarefa}')
    sleep(tempo_espera)
    print(f'Conclusao da tarefa {nome_tarefa}')
t1=Thread(target=tarefa,args=(3,'A'))
t2=Thread(target=tarefa,args=(2,'B'))
t1.start()
t2.start()
t1.join()
t2.join()
print("A execução foi concluida")