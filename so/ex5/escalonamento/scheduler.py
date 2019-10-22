import random
import operator

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

n = int(input("Qual a quantidede de processos?"))
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
