#include <stdio.h>

int main () {
    int num, quadrado;

    printf("Entre com o número: ");
    scanf("%d", &num);

    while (num != 0){
    quadrado = num * num;
    printf("O quadrado do número é: %d\n", quadrado);
    printf("Entre com o número: ");
    scanf("%d", &num);
    }
 }
