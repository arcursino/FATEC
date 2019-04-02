#include <stdio.h>

int main(){
    int a[] = {9,9, 9, 9, 9, 9, 9, 9, 9, 9};
    int b[] = {8, 8, 8, 8, 8, 8, 8, 8};
    int vazio = 1;

    for (int i = 0; i <= 9; i++) {
        for(int j = 0; j <= 7; j++){
            if (a[i] == b[j]){
                printf("%d\n", b[j]);
                vazio = 0;
            }
        }
    }

    if (vazio){
        printf("vazio\n");
    }
}
