#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 

int main (){ 
    int cont, i; 
    char str[100]; 

    puts("Digite uma palavra: "); 
    gets(str); 
    cont = strlen(str); 

    for (i=cont; i>=0; i--){ 
        printf("%c", str[i]);
    }
    printf("\n");
    return 0; 
} 
