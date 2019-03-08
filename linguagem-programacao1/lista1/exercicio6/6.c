#include <stdio.h>

int main(){
    int n, num, soma, i;

    printf("Quantos números: ");
    scanf("%d", &n);

    soma = 0;

    for (i = 1; i < n; i++){
        printf("Qual número: ");
        scanf("%d", &num);

        if (num % 2 == 0){
            soma += num;
        }
    }

    printf("%d\n", soma);
}

