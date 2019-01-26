#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "../../mylib_C/mylib.h"

/* Function prototype declaration */
bool isAnagram(char* s, char* t);
int loop_main(char* arg);

bool isAnagram(char* s, char* t)
{
    if (strlen(s) != strlen(t))
        return false;

    if (*s == '\0' || *t == '\0')
        return true;

    int dic_st['z' - 'a' + 1];
    for (int i = 0; i < 'z' - 'a' + 1; ++i)
        dic_st[i] = 0;

    char *work_s = s;
    char *work_t = t;

    while (*work_s != '\0') {
        if ('a' <= *work_s && *work_s <= 'z')
            dic_st[*work_s -  'a']++;
        else
            return false;
        work_s++;
    }

    while (*work_t != '\0') {
        if ('a' <= *work_t && *work_t <= 'z') {
            if (dic_st[*work_t -  'a'] == 0)
                return false;
            dic_st[*work_t -  'a']--;
        }
        else
            return false;
        work_t++;
    }

    return true;
}

int loop_main(char* arg)
{
    replace(arg, "[", "");
    replace(arg, "]", "");
    replace(arg, "\"", "");
    replace(arg, "\n", "");

    char* flds[2];
    int flds_length = split(arg, ",", flds, sizeof(flds)/sizeof(flds[0]));

    char *s, *t;
    if (arg[0] != '\0') {
        s = flds[0];
        t = flds[1];
    } else {
        s = "";
        t = "";
    }

    printf("s = %s, t = %s\n", s, t);

    clock_t time_start = clock();

    bool result = isAnagram(s, t);

    clock_t time_end = clock();

    if (result)
        printf("result = true\n\n");
    else
        printf("result = false\n\n");

    printf("Execute time ... %.0f ms\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // char* flds[] free().
    p_char_array_free(flds, flds_length);

    return 0;
}

int main(int argc, char *argv[])
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
