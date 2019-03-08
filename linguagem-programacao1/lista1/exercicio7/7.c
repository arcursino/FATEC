#include <stdio.h>

int main (){
    int n, fat, i;

    printf("Digite um número positivo: ");
    scanf("%d", &n);

    fat = 1;

    for (i = 0; i != n; i++){
        fat *= n - i;
    }

    printf("n!: %d\n", fat);
}
