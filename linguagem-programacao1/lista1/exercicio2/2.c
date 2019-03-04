#include <stdio.h>

int main() {
    int n, i, soma;

    printf("Escolha um número positivo: ");
    scanf("%d", &n);
    i = 1;
    soma = 0;

    while(i <= n){
        soma = i + soma;
        i++;
    }

    printf("Soma: %d\n", soma);

}
