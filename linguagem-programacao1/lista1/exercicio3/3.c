#include <stdio.h>

int main() {
    int n, imp, i;

    printf("Digite um número: ");
    scanf("%d", &n);

    imp = 1;

    for(i = 1;i <= n; i++) {
        printf("%d\n", imp);
        imp += 2;
    }
}
