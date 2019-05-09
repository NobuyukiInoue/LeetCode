#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "../../mylib_C/mylib.h"

/* Function prototype declaration */
bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n);
int loop_main(char* arg);

bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n)
{
    if (flowerbedSize == 0)
        return false;
    if (n == 0)
        return true;
    
    int plant = 0;
    for (int i = 0; i < flowerbedSize; ++i)
    {
        if (flowerbed[i] == 1)
            continue;
        if (i != 0)
            if (flowerbed[i - 1] == 1)
                continue;
        if (i != flowerbedSize - 1) 
            if (flowerbed[i + 1] == 1)
                continue;
        plant += 1;
        flowerbed[i] = 1;
    }

    return (n <= plant);
}

int loop_main(char* arg)
{
    int argv_length = strlen(arg);
    char* flds[2];
    char* str_nums[256];
    int flowerbed[256];

    replace(arg, "[[", "");
    replace(arg, "]]", "");
    replace(arg, "\n", "");
    int flds_length = split(arg, "],[", flds, sizeof(flds)/sizeof(flds[0]));
    int str_nums_length = split(flds[0], ",", str_nums, sizeof(str_nums)/sizeof(str_nums[0]));

    // int nums[] size check.
    if (sizeof(flowerbed)/sizeof(flowerbed[0]) < str_nums_length)
        err_exit("nums[] size error.");

    int flowerbetSize = str_to_int_array(str_nums, flowerbed, str_nums_length);
    int n = atoi(flds[1]);

    clock_t time_start = clock();
    bool results = canPlaceFlowers(flowerbed, flowerbetSize, n);
    clock_t time_end = clock();

    // result print.
    if (results)
        printf("result = true\n");
    else
        printf("result = false\n");

    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // char* str_nums[] free().
    p_char_array_free(str_nums, str_nums_length);

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
