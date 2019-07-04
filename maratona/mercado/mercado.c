// tags:

#include <stdio.h>

int main() {
    int n, i;

    scanf("%d\n", &n);

    int num[n];

    while ((i < n) && n != 0) {
        scanf("%d", &num[i]);
        i++;
    }

    return 0;
}
