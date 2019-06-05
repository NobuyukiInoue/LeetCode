#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "../../../mylib_C/mylib.h"

/* Function prototype declaration */
int strStr(char* haystack, char* needle);
int loop_main(char* arg);

int strStr(char* haystack, char* needle)
{
    if (*needle == '\0') {
        return 0;
    }

    if (*haystack == '\0') {
        return -1;
    }

    int len1, len2;
    int i, j, n;
    
    len1 = strlen(haystack);
    len2 = strlen(needle);
    
    for ( i = 0 ; i < len1; i++ ) {
        for ( n = i, j = 0; j < len2; j++, n++ ) {
            if ( n >= len1 ) {
                return -1;
            }

            if ( haystack[n] != needle[j] ) {
                break;
            }
        }

        
        if ( j == len2 ) {
            return i;
        }
    }

    return -1;
}

int loop_main(char* arg)
{
    int argv_length = strlen(arg);
    char* flds[2];

    replace(arg, "\"", "");
    replace(arg, "[[", "");
    replace(arg, "]]", "");
    replace(arg, "\n", "");

    int flds_length = split(arg, "],[", flds, sizeof(flds)/sizeof(flds[0]));
    char* hayhack = flds[0];
    char* needle = flds[1];

    clock_t time_start = clock();
    int results = strStr(hayhack, needle);
    clock_t time_end = clock();

    // result print.
    printf("result = %d\n", results);
    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // char* flds[] free().
    p_char_array_free(flds, flds_length);

    return 0;
}

int main(int argc, char* argv[])
{
#define fgets_MAX   65536
    FILE *fp;
    char line[fgets_MAX];

    if (argc < 2) {
        printf("Usage %s <testdatafile>\n", argv[0]);
        return -1;
    }

    // File Open
    fp = fopen(argv[1], "r");

    if (fp == NULL) {
        printf("%s Open Failed...\n", argv[1]);
        return -1;
    }

     while((fgets(line, fgets_MAX - 1, fp)) != NULL) {
        trim(line);
        if (*line == '\0')
            continue;
        printf("arg = %s\n", line);
        loop_main(line);
    }

    fclose(fp);
    return 0;
}
