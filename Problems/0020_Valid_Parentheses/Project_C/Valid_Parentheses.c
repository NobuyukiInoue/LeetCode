#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "../../mylib_C/mylib.h"

/* Function prototype declaration */
bool isValid(char* s);

char* output_list(char **list, int list_Length);
int loop_main(char* arg);

bool isValid(char* s)
{
    char stack[65535];
    int i = 0, n = 0;
    int s_len;

    s_len = strlen(s);
    
    for (i = 0; i < s_len; i++ ) {

        if ( n < 0 )
            return false;

        if ( s[i] == '(' )
            stack[n++] = s[i];
        else if ( s[i] == '{' ) 
            stack[n++] = s[i];
        else if ( s[i] == '[' )
            stack[n++] = s[i];
        else if ( n > 0 )
            if ( s[i] == ')' && stack[n - 1] == '(' )
                --n;
            else if ( s[i] == '}' && stack[n - 1] == '{' )
                --n;
            else if ( s[i] == ']' && stack[n - 1] == '[' )
                --n;
            else
                return false;
        else
            return false;
    }

    if ( n == 0 )
        return true;
    else
        return false;
}

int loop_main(char* arg)
{
    #define nums_MAX_SIZE   256

    int argv_length = strlen(arg);
    char s[1024];

    strcpy(s, arg);
    replace(s, "\"", "");
    replace(s, "\n", "");

    clock_t time_start = clock();
    bool result = isValid(s);
    clock_t time_end = clock();

    // result print.
    if (result)
        printf("result = true\n");
    else
        printf("result = false\n");

    printf("Execute time ... %.0f ms\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    return 0;
}

int main(int argc, char* argv[])
{
    FILE *fp;
    char str[256];

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

    while((fgets(str, 256, fp)) != NULL) {
        printf("arg = %s\n", str);
        loop_main(str);
    }

    fclose(fp);
    return 0;
}
