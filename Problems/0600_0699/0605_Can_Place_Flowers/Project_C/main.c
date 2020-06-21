#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "include/mylib.h"

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
    ml_replace(arg, "[[", "");
    ml_replace(arg, "]]", "");
    ml_replace(arg, "\n", "");

    char* flds[2];
    int flds_length = ml_split(arg, "],[", flds, sizeof(flds)/sizeof(flds[0]));

    int *flowerbed;
    int flowerbetSize = ml_str_to_int_array(flds[0], &flowerbed);
	ml_print_int_array("flowerbed", flowerbed, flowerbetSize);

    int n = strtol(flds[1], NULL, 10);
    printf("n = %d\n", n);

    clock_t time_start = clock();

    bool results = canPlaceFlowers(flowerbed, flowerbetSize, n);

    clock_t time_end = clock();

    // result print.
    if (results)
        printf("result = true\n");
    else
        printf("result = false\n");

    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // int nums[] clear.
    free(flowerbed);

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
