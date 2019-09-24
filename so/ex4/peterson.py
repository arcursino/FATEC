#Solução de Peterson
from threading import Thread
import time

global turn, i, j, flag

def regiaoCritica():
    time.sleep(1)

def processamentoA(times, delay):
    global turn, i, j, flag
    for x in range(times):
        print ("Secao de Entrada A - ",x+1)  
        flag[i] = True
        turn = j
        while (flag[j] and turn == j):
            continue
        print ("Regiao Critica A")
        regiaoCritica()
        print ("Secao de Saida A")
        flag[i] = False
        print ("Regiao nao critica A\n")
        time.sleep(delay)    

def processamentoB(times, delay):
    global turn, i, j, flag
    for x in range(times):
        print ("Secao de Entrada B - ",x+1)
        flag[j] = True
        turn = i        
        while (flag[i] and turn == i):
            continue
        print ("Regiao Critica B")        
        regiaoCritica()
        print ("Secao de Saida B")
        flag[j] = False
        print ("Regiao nao critica B\n")
        time.sleep(delay)


print ("Exemplo de Solucao de Peterson")
execTimes = 5
turn = 0
i = 0
j = 1
flag = []
flag.append(False)
flag.append(False)

#no processamento você pode passar quantas vezes que a exec e
#qual o tempo de delay para simular o efeito comboio
tA = Thread(target=processamentoA, args=(execTimes,1,))
tA.start()
tB = Thread(target=processamentoB, args=(execTimes,5,))
tB.start()