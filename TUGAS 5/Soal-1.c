#include <stdio.h>

int main(void) {
    char teks[200];
    int jumlah[26] = {0};
    int i;

    printf("Masukkan sebuah kalimat atau nama: ");
    scanf("%199[^\n]", teks);

    for (i = 0; teks[i] != '\0'; i++) {
        if (teks[i] >= 'A' && teks[i] <= 'Z')
            jumlah[teks[i] - 'A']++;
        else if (teks[i] >= 'a' && teks[i] <= 'z')
            jumlah[teks[i] - 'a']++;
    }

    printf("\nFrekuensi huruf:\n");
    for (i = 0; i < 26; i++) {
        if (jumlah[i] > 0)
            printf("%c = %d\n", 'a' + i, jumlah[i]);
    }

    return 0;
}
