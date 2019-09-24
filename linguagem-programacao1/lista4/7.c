#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 

int main() {
    char nome[100], aux[100], m; 
    int i, cont=0, v=0, c=0, e=0, p=0; 

    puts("Digite seu nome: "); 
    gets(nome); 
    printf ("Escolha uma letra: "); 
    scanf ("%c", &m); 

    for (i=0; nome[i] !='\0'; i++) {
        cont++; 
        
        if (nome[i]=='a'||nome[i]=='e'||nome[i]=='i'||nome[i]=='o'||nome[i]=='u') { 
            v++;
        } 
        if (nome[i]=='b'||nome[i]=='c'||nome[i]=='d'||nome[i]=='f'||nome[i]=='g'||nome[i]=='h'||nome[i]=='j'|| nome[i]=='k'||nome[i]=='l'||nome[i]=='m'||nome[i]=='n'||nome[i]=='p'||nome[i]=='q'||nome[i]=='r'||nome[i] =='s'|| nome[i]=='t'||nome[i]=='v'||nome[i]=='x'||nome[i]=='w'||nome[i]=='y'||nome[i]=='z') { 
            c++; 
            aux[i] = nome[i];
        } 
        if (nome[i]== ' ') { 
            e++;
        } 
        if (nome[i] == m) {
            nome[i]='*'; 
        } 
        printf("%c\n nome[i]); 
    } 
    printf("Quantidade de caracteres: %d\n", cont); 
    printf("Quantidade de vogais: %d\n", v); 
    printf("Quantidade de consoantes: %d\n", c); 
    printf("Quantidade de espacos vazios: %d\n", e); 
    
    for (i=0, p=0; i<cont; p++, i++) {
        if(aux[p]==' ') {
            p++;
        } 
        aux[i]=aux[p]; 
        printf("%c", aux[i]);
    }
    return 0; 
} 
