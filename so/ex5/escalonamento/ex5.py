import random
import operator
from itertools import *

class Processo(object):
    def __init__(self, nome,burst,tcheg):
        self.nome = nome
        self.burst = burst
        self.tcheg = tcheg
    
    def setNome(nome):
        self.nome = nome

    def setBurst(burst):
        self.burst = burst
    
    def setTcheg(tcheg):
        self.tcheg = tcheg

n = int(input("Qual a quantidade de processos?"))
lista = []

c = input("Burst manual ou aleatório(M/A)?")

if c == "A":
    #burst e tempo de chegada automático
    for i in range(n):
        proc = Processo(i,random.randint(1, 100),random.randint(0, 15))
        lista.append(proc)
else:
    #burst e tempo de chegada manual
    for i in range(n):
        b = int(input("P" + str(i) +" Burst:"))
        t = int(input("P" + str(i) +" Tempo de Chegada:"))
        proc = Processo(i,b,t)
        lista.append(proc)

print ("Todos os processos...")
print ("proc","burst","tcheg")
for i in lista:
    print(i.nome," ", i.burst," ",i.tcheg)

#ordenando os objetos pelo burst
print(" ")
print("Objetos ordenados pelo burst")
lista.sort(key=operator.attrgetter("burst"),reverse=False)
print ("proc","burst",)
for i in lista:
    print(i.nome," ", i.burst)

#ordenando os objetos pelo tempo de chegada
print(" ")
print("Objetos ordenados pelo tempo de chegada")
lista.sort(key=operator.attrgetter("tcheg"),reverse=False)
print ("proc","burst","tcheg")
for i in lista:
    print(i.nome," ", i.burst," ",i.tcheg)


def srtf():
    n = int(input('Qual a quantidade de processos? '))
    bt = [0] * (n + 1)
    at = [0] * (n + 1)
    abt = [0] * (n + 1)
    for i in range(n):
        abt[i] = int(input('Enter the burst time for process {} : '.format(i + 1)))
        at[i] = int(input('Enter the arrival time for process {} : '.format(i + 1))) 
        bt[i] = [abt[i], at[i], i]

    #bt = [[7, 0, 7, 0], [5, 1, 5, 1], [3, 2, 3, 2], [1, 3, 1, 3], [2, 4, 2, 4], [1, 5, 1, 5]]
    #at = [0, 1, 2, 3, 4, 5]
    bt.pop(-1)
    print(abt)
    print(bt)
    sumbt = 0 
    i = 0
    ll = []
    for i in range(0, sum(abt)):
        l = [j for j in bt  if j[1] <= i]
        l.sort(key=lambda x: x[0])
        print(l, l[0][2])
        bt[bt.index(l[0])][0] -= 1
    for k in bt:
        if k[0] == 0:
            t = bt.pop(bt.index(k))
            ll.append([k, i + 1])
    print(ll)
    ct = [0] * (n + 1)
    tat = [0] * (n + 1)
    wt = [0] * (n + 1)
    for i in ll:
        print(i, i[0], i[1], i[0][2])
        ct[i[0][2]] = i[1] 
        #abt[i[0][3]] = i[0][2]

    for i in range(len(ct)):
        tat[i] = ct[i] - at[i]
        wt[i] = tat[i] - abt[i]
        ct.pop(-1)
        wt.pop(-1)
        tat.pop(-1)
        abt.pop(-1)
        at.pop(-1)
        print('BT\tAT\tCT\tTAT\tWT')
    for i in range(len(ct)):
        print("{}\t{}\t{}\t{}\t{}\n".format(abt[i], at[i], ct[i], tat[i], wt[i]))
        print('Average Waiting Time = ', sum(wt)/len(wt))
        print('Average Turnaround Time = ', sum(tat)/len(tat))


class Round_Robin():

    def __init__(self,data):
        self.data = data
        self.data_rr = self.get_item()

    def cycle(self,iterable):
        saved = []
        for element in iterable:
            yield element
            saved.append(element)
        while saved:
            for element in saved:
                yield element

    def get_item(self):
        count = 0
        for item in self.cycle(self.data):
            count += 1
            yield (count, item)

    def get_next(self):
        return self.data_rr.next()
        

if __name__ == "__main__":
    rr_obj = Round_Robin(['a','b','c'])
    for i in range(50):
        print rr_obj.get_next()

