/* Deliberately flawed, locally owned teaching program.
   Run only in your isolated learning VM. */
#include <stddef.h>
#include <stdio.h>
int parse(const unsigned char *buf, size_t size) {
    if (size == 0) return -1;
    size_t length = buf[0];
    /* Teaching defect: length is not checked against size. */
    unsigned int total = 0;
    for (size_t i = 0; i < length; ++i) total += buf[i + 1];
    return (int)total;
}
int main(void) {
    const unsigned char valid[] = {2, 10, 20};
    const unsigned char truncated[] = {3, 10};
    printf("valid=%d\n", parse(valid, sizeof(valid)));
    printf("truncated=%d\n", parse(truncated, sizeof(truncated)));
    return 0;
}
