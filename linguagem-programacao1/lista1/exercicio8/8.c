#include <stdio.h>

int main () {
    int n, i, j, somai, somaj;

    printf("Digite o valor de n: ");
    scanf("%d", &n);

    printf("Digite o valor de i: ");
    scanf("%d", &i);

    printf("Digite o valor de j: ");
    scanf("%d", &j);

    somai = 0;
    somaj = 0;

    /*while (i <= n){
        if (i % 2 == 0 ){
            somai += i;
        }

    while (j <=n){
        if (i % 2 == 0 ){
            somaj += j;
        }
    }

    printf("Saída: %d\n", somai, somaj);

    }
}*/




    for (i = 1; i < n; i++){
        if (i % 2 == 0 ){
            somai += i;
        }
    }

    for (j = 1; j < n; j++){

        if (j % 2 == 0){
            somaj += j;
        }
    }

    printf("Saída: %d\n", somai, somaj);

}

