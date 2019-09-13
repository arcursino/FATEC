#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

int main () {
    int pid;

    //põe a função fork em uma variável
    pid = fork();

    // Se n for menor que 0, significa que tem um erro.
    if (pid < 0) {
        printf (stderr, "Erro\n");
        exit(1);
    }
    // Se n for igual a 0, significa que o processo é "filho".
    if (pid == 0) {
        printf("Filho:\t id is %d, pid(valor)is %d\n", getpid(), pid);
    }
    // Se o pid é maior que 0, significa que o processo é "pai". 
    else {
        ("Pai: \t is %d, pid(filho)is %d\n", getpid(), pid);
        system("date");
    }
}
