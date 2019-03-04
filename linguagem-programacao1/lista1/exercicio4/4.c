#include <stdio.h>

int main() {
    int x, n, i;

    printf("Escolha uma base: ");
    scanf("%d", &x);

    printf("Escolha uma potência: ");
    scanf("%d", &n);

    int aux = 1;

    for (i = 1; i <= n; i++){
        aux *=  x;
     }

    printf("%d\n", aux );
}

