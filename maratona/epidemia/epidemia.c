// tags: iniciante, maratona

#include <stdio.h>

int main() {
    int a, b, c;

    scanf("%d %d %d", &a, &b, &c);

    if (a < b && a < c) {
        printf("%d\n", a);
    }
    if (b < c && b < a) {
        printf("%d\n", b);
    }
    if (c < b && c < a) {
        printf("%d\n", c);
    }
    if (a == b && a == c && b == c) {
        printf("%d\n", a);
    }

    return 0;
}
