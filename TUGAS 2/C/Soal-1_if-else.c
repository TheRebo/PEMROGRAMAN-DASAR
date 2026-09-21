#include <stdio.h>

int main() {
    int nilai;

    printf("Masukkan nilai: ");
    scanf("%d", &nilai);

    if (nilai >= 80) {
        printf("Grade A");
    } else if (nilai >= 70) {
        printf("Grade B");
    } else if (nilai >= 60) {
        printf("Grade C");
    } else if (nilai >= 50) {
        printf("Grade D");
    } else {
        printf("Grade E");
    }

    return 0;
}
