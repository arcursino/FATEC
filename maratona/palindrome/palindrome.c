#include <stdio.h>
#include <string.h>

int main(){
    int n, i;
    char a[26], b[26];

    scanf("%d", &n);
    fgets(a);

    for(i = 0; i < n; i++){
        strcpy(b,a);
        b = rev(b);

        if(strcmp(a,b) == 0){
            printf("sim");
        } else {
            printf("nao");
        }
    }
}

