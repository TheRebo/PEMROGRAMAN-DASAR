#include <stdio.h>

int main() {
    int nilai;

    printf("Masukkan nilai: ");
    scanf("%d", &nilai);

    switch (nilai) {
        case 80 ... 100:
            printf("Grade A");
            break;
        case 70 ... 79:
            printf("Grade B");
            break;
        case 60 ... 69:
            printf("Grade C");
            break;
        case 50 ... 59:
            printf("Grade D");
            break;
        default:
            printf("Grade E");
    }

    return 0;
}
