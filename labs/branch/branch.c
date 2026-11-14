#include <stdio.h>
int classify(unsigned int value) {
    if (value < 16) return 1;
    return 0;
}
int main(void) {
    printf("%d %d\n", classify(15), classify(16));
    return 0;
}
