#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "../../mylib_C/mylib.h"

/* Function prototype declaration */
char** letterCombinations(char* digits, int* returnSize);

char* output_list(char **list, int list_Length);
int loop_main(char* arg);

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */

char map[10][4] = {
    {' ', ' ', ' ', ' '}, //0
    {' ', ' ', ' ', ' '}, //1
    {'a', 'b', 'c', ' '}, //2
    {'d', 'e', 'f', ' '}, //3
    {'g', 'h', 'i', ' '}, //4
    {'j', 'k', 'l', ' '},
    {'m', 'n', 'o', ' '},
    {'p', 'q', 'r', 's'},
    {'t', 'u', 'v', ' '}, //8
    {'w', 'x', 'y', 'z'} //9
};

void letterComb(char* digits, int* returnSize, char *result, int ind, char **ans)
{
    int i = 0;
    char c;
    char *letter = map[digits[0] - '0'];

    if (digits[0] == 0) {
        char *res = malloc(strlen(result) + 1);
        strcpy(res, result);
        ans[(*returnSize)] = res;
        (*returnSize)++;
        return;
    }

    while ((c = letter[i]) != ' ') {
        result[ind] = c;
        letterComb(digits + 1, returnSize, result, ind + 1, ans);
        i++;
        if (i == 4)
            break;
    }
    return;
}

char** letterCombinations(char* digits, int* returnSize)
{
    #define LEN 1024

    int ind = 0, size = 0;
    int len = strlen(digits) + 1;
    char result[LEN];
    
    if (digits == NULL || strlen(digits) == 0)
        return NULL;
  
    char **ans = (char **) malloc(sizeof (char *) * 32768);
        
    memset(result, 0, len);
    
    letterComb(digits, &size, result, ind, ans);
    *returnSize = size;
    
    return ans;
}

/*
char** letterCombinations(char* digits, int* returnSize)
{
    struct map {
        int index;
        char* character;
    };

    struct map my_dic[10] = {
        { 0, ""}, { 1, ""}, { 2, "abc"}, { 3, "def"}, { 4, "ghi"}, { 5, "jkl"}, { 6, "mno"}, { 7,"pqrs"}, { 8,"tuv"}, { 9,"wxyz"}
    };

    int index = 0;
    int character_Length = 0;
    int result_all_Length = 1;

    for (int n = 0; n < strlen(digits); ++n) {
        index = (int)(digits[n] - '0');
        if (index > 2) {
            character_Length = strlen(my_dic[index].character);
            result_all_Length *= character_Length;
        }
    }

    char** result = (char**)malloc(sizeof(char*)*result_all_Length);

    for (int n = 0; n < strlen(digits); ++n) {
        index = (int)(digits[n] - '0');

        if (index <= 2)
            continue;

        character_Length = strlen(my_dic[index].character);
        for (int i = 0; i < character_Length; ++i) {
            subset(my_dic, result[(result_all_Length/character_Length) * (i + 1)], i, digits, index);
        }
    }
}

int subset(struct map my_dic[], char** sub_result, int i, char* digits, int index)
{
    int character_Length = strlen(my_dic[index].character);
    for (int i = 0; i < character_Length; ++i) {
        subset(result[(result_all_Length/character_Length) * (i + 1)], digits, i);
    }
}
*/

char* output_list(char **list, int list_Length)
{
    #define result_MAX_SIZE 65536

    char* resultStr = (char*)malloc(sizeof(char)*result_MAX_SIZE);
    resultStr[0] = '\0';

    strcat(resultStr, "\"");
    strcat(resultStr, list[0]);
    strcat(resultStr, "\"");

    for (int i = 1; i < list_Length; ++i) {
        strcat(resultStr, ",\"");
        strcat(resultStr, list[i]);
        strcat(resultStr, "\"");
    }

    return resultStr;
}

int loop_main(char* arg)
{
    #define nums_MAX_SIZE   256

    int argv_length = strlen(arg);
    char digits[1024];
    int result_Length = 0;

    strcpy(digits, arg);

    replace(digits, "[", "");
    replace(digits, "]", "");
    replace(digits, "\"", "");
    replace(digits, "\n", "");

    clock_t time_start = clock();
    char** result = letterCombinations(digits, &result_Length);
    clock_t time_end = clock();

    // result print.
    printf("result = %s\n", output_list(result, result_Length));
    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

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
