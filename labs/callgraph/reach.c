/* Locally owned teaching program for call-graph reachability.
   legacy_decode holds the "weakness" a scanner would flag. Is it reachable? */
#include <stdio.h>
#include <string.h>

typedef int (*handler_fn)(const char *);

__attribute__((noinline)) int legacy_decode(const char *text) { return (int)strlen(text) * 2; }
__attribute__((noinline)) int modern_decode(const char *text) { return (int)strlen(text); }
__attribute__((noinline)) int audit_log(const char *text) { return printf("audit: %s\n", text); }
__attribute__((noinline)) int unused_export(const char *text) { return legacy_decode(text); }
__attribute__((noinline)) int plugin_entry(const char *text) { return legacy_decode(text) + 1; }

static handler_fn handlers[] = { modern_decode, plugin_entry };

__attribute__((noinline)) int dispatch(unsigned int kind, const char *text) {
    if (kind >= sizeof(handlers) / sizeof(handlers[0])) return -1;
    return handlers[kind](text); /* indirect call: target unknown to a direct-call graph */
}

int main(int argc, char **argv) {
    const char *text = argc > 1 ? argv[1] : "atlas";
    audit_log(text);
    printf("%d\n", dispatch(argc > 2, text));
    return 0;
}
