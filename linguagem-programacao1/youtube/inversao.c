#include <stdio.h>

int main () {
    int numero, cifra;

    scanf("%d", &numero);

    if (numero >= 0) {
        do {
            cifra = numero % 10;
            printf("%d", cifra);
            numero /= 10;

        } while (numero != 0);

    } else if (numero < 1) {
        numero = numero * -1;
        printf("-");

        do {
            cifra = numero % 10;
            printf("%d", cifra);
            numero /= 10;

        } while (numero != 0);
    }
    printf("\n");
}


