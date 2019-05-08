#include <stdio.h>

int main (){
    int a[] = {567890};
    int b[] = {890};
    int i, j;

    if (a[-1] == b[-1]){
        printf("1\n");
    }
    else{
        printf("0\n");
    }
}
