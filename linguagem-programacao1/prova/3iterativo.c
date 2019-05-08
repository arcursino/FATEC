#include <stdio.h>
#include <math.h>

int main(){
    int n, x, i;
    long soma;

    scanf("%d", &x);

    soma = 0;

    for (int n = 2; n < 2; n++){
        soma = ((n + 1) * pow(x, n)) / pow (2,n);
        soma += soma;
    }
    printf("%ld\n", soma);
}
