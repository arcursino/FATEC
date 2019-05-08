#include <stdio.h>
#include <math.h>

unsigned long long algo(int x) {
    long sumation = 0;
    for (int n = 0; n <= 100; n++) {
        sumation += ((n + 1) * pow(x, n)) / pow(2, n);
    }

    return sumation;
}

unsigned long long algo_recursivo(int x, int n) {
    if (n == 0) {
        return 1;
    }
    return ((n + 1) * pow(x, n)) / pow(2, n) + algo_recursivo(x, n - 1);
}

long soma(int x, int n){
    if (n == 0){
        return 1;
    }
    return (n - 1) + (((n + 1)/ n) * x) * (soma(x, n - 1) / 2);
}

int sum(int n) {
    if (n == 0) {
        return 0;
    }
    return n + sum(n - 1);
}

int main(){
    int x;

    printf("iter %llu\n", algo(1));
    printf("rec %llu\n", algo_recursivo(1, 100));
    //printf("%ld\n", soma(2, 4));
    //printf("%d\n", sum(3));
    //printf("%d\n", sum(6));
}
