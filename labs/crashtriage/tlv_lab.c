/* Deliberately flawed, locally owned teaching program.
   Run only in your isolated learning VM.
   Record: magic "ATLS" (4) | type (1) | len (1) | payload (len)
   Builds: default = file reader, -DFUZZ = libFuzzer harness,
           -DFIX_A / -DFIX_B = repair one teaching defect,
           -DFIXED = repair both. */
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifdef FIXED
#define FIX_A
#define FIX_B
#endif

int tlv_parse(const uint8_t *buf, size_t size) {
    if (size < 6) return -1;
    if (memcmp(buf, "ATLS", 4) != 0) return -2;
    uint8_t type = buf[4];
    size_t len = buf[5];
    const uint8_t *payload = buf + 6;
    switch (type) {
    case 1: { /* checksum record */
#ifdef FIX_A
        if (len > size - 6) return -3;
#endif
        /* Teaching defect A: len is not checked against size. */
        unsigned int total = 0;
        for (size_t i = 0; i < len; ++i) total += payload[i];
        return (int)(total & 0x7fff);
    }
    case 2: { /* label record */
        uint8_t label[8] = {0};
        if (len > size - 6) return -3;
#ifdef FIX_B
        if (len > sizeof(label)) return -4;
#endif
        /* Teaching defect B: len is not checked against the label size. */
        memcpy(label, payload, len);
        return label[0];
    }
    case 3: { /* version record guarded by an arithmetic condition */
        if (len != 4 || size - 6 < 4) return -3;
        uint32_t v;
        memcpy(&v, payload, 4);
        if (((v ^ 0x5a5a5a5au) * 2654435761u) >> 7 == 0xddd54au) return 0x7777; /* gated path */
        return 0;
    }
    default:
        return -5;
    }
}

#ifdef FUZZ
int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
    /* Keep the result alive so the optimizer cannot delete the call. */
    static volatile int sink;
    sink = tlv_parse(data, size);
    return 0;
}
#else
int main(int argc, char **argv) {
    if (argc != 2) { fprintf(stderr, "usage: %s <record-file>\n", argv[0]); return 2; }
    FILE *f = fopen(argv[1], "rb");
    if (!f) { perror("fopen"); return 2; }
    uint8_t *buf = malloc(4096);
    if (!buf) { fclose(f); return 2; }
    size_t n = fread(buf, 1, 4096, f);
    fclose(f);
    /* Copy into an exact-size allocation so a sanitizer sees the real bound. */
    uint8_t *exact = malloc(n ? n : 1);
    if (!exact) { free(buf); return 2; }
    memcpy(exact, buf, n);
    free(buf);
    printf("result=%d\n", tlv_parse(exact, n));
    free(exact);
    return 0;
}
#endif
