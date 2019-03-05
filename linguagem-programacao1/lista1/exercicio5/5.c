#include <stdio.h>

int main(){
    int num, nota, i, max, min;

    printf("Entre com o número de alunos: ");
    scanf("%d", &num);

    max = -1;
    min = 11;

    i = 0;
    do {
        printf("Entre com a nota: ");
        scanf("%d",&nota);

        while (nota < 0 || nota > 10){
            printf("Número inválido, digite outro número: ");
            scanf("%d", &nota);
        }

        if (nota < min) {
            min = nota;
        }
        if (nota > max) {
            max = nota;
        }

        i++;
    } while (i < num);

    printf("Nota mínima = %d\n", min);
    printf("Nota máxima = %d\n", max);
}
