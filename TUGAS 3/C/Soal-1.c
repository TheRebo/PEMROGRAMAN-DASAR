#include <stdio.h>

int main(void) {
    int batas;
    int total = 0;

    printf("Masukan batas maksimal: ");
    scanf("%d", &batas);

    printf("\nOutput: ");
    for (int i = 1; i <= batas; i++) {
        total += i;
        printf(i < batas ? "%d + " : "%d", i);
    }
    printf(" = %d", total);

    return 0;
}
