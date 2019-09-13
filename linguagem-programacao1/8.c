#include <stdio.h>

int num(n);

int main() {
    int n;

    printf("Digite um numero positivo: ");
    scanf("%d\n", &n);

    num(n);
}

int num(int n) {
    if (n % 2 == 0){
        return 1;
    } else {
        return 0;
    }    
}