/*Criar um programa que solicita no teclado uma frase com, no máximo, 100 letras.
    Se o tamanho for maior que 40, exibir uma mensagem e solicitar novamente a
    frase, senão, imprimir a frase na vertical.*/

#include <stdio.h> 
#include <stdlib.h> 
#include <math.h> 

int main() {
    int cont, i; 
    char str[100]; 

    puts("Digite uma frase: "); 
    gets(str); 
    cont = strlen(str); 

    if (cont > 40) {
        printf("Digite outra frase por favor:");
    }else {
        for (i=cont; i>=0; i--) { 
        printf("%c\n", str[i]);
        }
    } 
    return 0; 
}


