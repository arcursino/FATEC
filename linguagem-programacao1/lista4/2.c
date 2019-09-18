#include <stdio.h>

int main() {
    int linha, coluna;
    int matriz[5][5];

    for (linha=0;linha<5;linha++){
        for (coluna=0;coluna<5;coluna++){
            if (linha == coluna){
                matriz[linha][coluna] = 1;
            } else {
                matriz[linha][coluna] = 0;
            }
        }
    }

    for (linha=0;linha<5;linha++){
        for (coluna=0;coluna<5;coluna++){
            printf("[ %d ] ", matriz[linha][coluna]);
        }
        printf("\n");
    }
    return 0;
}