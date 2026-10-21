#include <stdio.h>

int main() {
    int jumlah;
    char array[jumlah];

    printf("Masukan jumlah/isi array: ");
    scanf("%d", &jumlah);

    for (int i = 0; i < jumlah; i++) {
        printf("Masukan index ke-%d: ", i);
        scanf(" %c", &array[i]);
    }

    for (int i = 0; i < jumlah; i++) {
        printf("%c ", array[i]);
    }

    return 0;
}
