#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "include/mylib.h"
#include "include/operate_stack.h"

/* Function prototype declaration */
int calc(char* cmds[], char *argvals[], int cmds_length);
int loop_main(char* arg);

int calc(char* cmds[], char *argvals[], int cmds_length) {
    MyStack *obj;
    bool createdStack = false;

    for (int i = 0; i < cmds_length; i++) {

        if (strcmp(cmds[i], "MyStack") == 0) {
            createdStack = true;
            obj = myStackCreate();

        } else {
            if (createdStack != true) {
                printf("MyStack was not created.\n");
                return -1;
            }

            int val = strtol(argvals[i], NULL, 10);

            if (strcmp(cmds[i], "push") == 0) {
                myStackPush(obj, val);
                printf("Push(%d)\n", val);

            } else if (strcmp(cmds[i], "pop") == 0) {
                int result = myStackPop(obj);
                printf("Pop() ... %d\n", result);

            } else if (strcmp(cmds[i], "top") == 0) {
                int result = myStackTop(obj);
                printf("Top() ... %d\n", result);

            } else if (strcmp(cmds[i], "empty") == 0) {
                int result = myStackEmpty(obj);
                printf("Empty() ... %s\n", (result == 1 ? "true": "false"));
            }
        }
    }
}

int loop_main(char* arg)
{
    ml_replace(arg, "\"", "");
    ml_replace(arg, "\n", "");

    char* flds[2];
    int flds_length = ml_split(arg, "],[[", flds, sizeof(flds)/sizeof(flds[0]));

    char** cmds;
    ml_replace(flds[0], "[[", "");
    int cmds_length = ml_str_to_pchar_array(flds[0], &cmds);
    ml_print_pchar_array("cmds", cmds, cmds_length);

    char** argvals;
    ml_replace(flds[1], "[", "");
    ml_replace(flds[1], "]", "");
    int argvals_length = ml_str_to_pchar_array(flds[1], &argvals);
    ml_print_pchar_array("argvals", argvals, argvals_length);

    clock_t time_start = clock();

    calc(cmds, argvals, cmds_length);

    clock_t time_end = clock();

    // result print.
    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // char* argvals[] clear.
    ml_p_char_array_free(argvals, argvals_length);

    // char* cmds[] clear.
    ml_p_char_array_free(cmds, cmds_length);

    // char* flds[] clear.
    ml_p_char_array_free(flds, flds_length);

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

    while ((fgets(line, fgets_MAX - 1, fp)) != NULL) {
        ml_trim(line);
        if (*line == '\0')
            continue;
        printf("arg = %s\n", line);
        loop_main(line);
    }

    fclose(fp);
    return 0;
}
