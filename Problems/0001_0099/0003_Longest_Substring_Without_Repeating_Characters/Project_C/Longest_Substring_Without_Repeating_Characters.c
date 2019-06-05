#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "../../../mylib_C/mylib.h"

/* Function prototype declaration */
int lengthOfLongestSubstring(char* s);
int loop_main(char* arg);


int lengthOfLongestSubstring(char* s)
{
	int length = 0;
    char *end = s, *temp;
	char* addressTable[128] = { NULL };

	while (*end) {
		temp = addressTable[*end];
		addressTable[*end] = end;
		if (temp >= s) {
		    length = end-s > length? end-s: length;
		    s = temp + 1;
		}
        end++;
	}

	length = end - s > length? end-s:length;
	return length;
}

int loop_main(char* arg)
{
    #define nums_MAX_SIZE   256

    int argv_length = strlen(arg);
    char s[1024];

    strcpy(s, arg);

    replace(s, "[", "");
    replace(s, "]", "");
    replace(s, "\"", "");
    replace(s, "\n", "");

    clock_t time_start = clock();
    int result = lengthOfLongestSubstring(s);
    clock_t time_end = clock();

    // result print.
    printf("result = %d\n", result);
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
