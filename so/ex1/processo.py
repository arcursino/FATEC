#Importar o módulo "os" que traz informações sobre o sistema operacional
import os 
  
def parent_child():
    #põe a função fork em uma variável 
    n = os.fork() 
  
    # Se o n é maior que 0, significa que o processo é "pai". 
    if n > 0: 
        #informa qual é o processo e seu id
        print("Parent process and id is : ", os.getpid()) 
  
    # Se n for igual a 0, significa que o processo é "filho". 
    else: 
        #informa qual é o processo e seu id
        print("Child process and id is : ", os.getpid()) 
          
# chama a função 
parent_child() 