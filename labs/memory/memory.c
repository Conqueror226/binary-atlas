#include <stdio.h>
int main(void) {
    unsigned char bytes[4] = {0x41, 0x42, 0x43, 0x00};
    unsigned char *p = bytes;
    printf("first=%u second=%u size=%zu\n", p[0], p[1], sizeof(bytes));
    return 0;
}
