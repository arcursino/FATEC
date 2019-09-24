#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 

int palindromo (char palavra[], int tam, int posicao) { 
    if (palavra[posicao]==palavra[tam-posicao-1]) { 
        return 1; 
    } else {
        return 0; 
    } 
} 

int main (){ 
    int tam; 
    char palavra[50]; 

    puts("Digite uma palavra: "); 
    gets(palavra); 

    tam = strlen(palavra);

    if (palindromo(palavra, tam, 0)) {
        printf("É palindromo\n");
        } else { 
            printf("Não é palindromo\n"); 
        }
        return 0; 
} 
