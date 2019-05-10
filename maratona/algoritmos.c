//primos
#include <stdio.h>
#include <math.h>

int eh_primo(int numero) {
    if (numero == 2) {
        return 1;
    }
    if (numero % 2 == 0) {
        return 0;
    }
    for (int i = 3; i <= sqrt(numero); i += 2) {
        if (numero % i == 0) {
            return 0;
        }
    }
    return 1;
}

// fibonacci, memoize
long long fib_memoize[61];

long long fib(int n) {
    if (fib_memoize[n] != -1) {
        return fib_memoize[n];
    }
    if (n == 0 || n == 1) {
        return n;

    } else {
        fib_memoize[n] = fib(n - 1) + fib(n - 2);
    }
    return fib_memoize[n];
}

// fatorial
int fat(int n) {
    if (n == 0) {
        return n + 1;

    } else {
        return n * fat(n-1);
    }
}

// mdc
int maximo_divisor_comum(int x, int y) {
    if (y == 0) {
        return x;
    }
    return maximo_divisor_comum(y, x % y);
}

// mmc
long minimo_multiplo_comum(int x, int y) {
    return abs(x) / maximo_divisor_comum(x, y) * abs(y);
}

//busca binária
int cont = 0;
int busca_binaria(int numeros[], int busca, int tamanho) {
    int inicio = 0;
    int fim = tamanho - 1;
    int metade = tamanho / 2;

    while (inicio <= fim) {
        if (busca == numeros[metade]) {
            return metade;
        } else if (numeros[metade] < busca) {
            inicio = metade + 1;
        } else {
            fim = metade - 1;
        }
        cont++;

        metade = inicio + (fim - inicio) / 2;

    }

    return -1;
}

int main() {
    int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16};
    printf("%d\n", busca_binaria(a, 2, 16));

    printf("s cont: %d\n", cont);
}
