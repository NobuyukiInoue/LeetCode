#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "../../mylib_C/mylib.h"

/* Function prototype declaration */
int countPrimes(int n);
int countPrimes_work(int n);
int loop_main(char* arg);

int countPrimes(int n)
{
    if (n < 3)
        return 0;
    const int sievebound = (n - 1) >> 1,
            crossn = ((int)sqrt(n) - 1) >> 1;
    _Bool* sieve = calloc(sievebound + 1, 1);
    int i, j, res = 0;

    for (i = 1; i <= crossn; i++)
    if (!sieve[i])
        for (j = i * (i + 1) << 1; j <= sievebound; j += (i << 1) + 1)
        sieve[j] = 1;
        
    for (i = 1 ; i < n; i += 2)
        res += !sieve[i>>1];
    return res;
}

int countPrimes_work(int n)
{
    if (n <= 2)
        return 0;
    if (n == 3)
        return 1;
    
    bool* checked_prime_flag = (bool *)calloc(sizeof(bool), n);
    int i, j, count = 1;

    for (i = 2; i < n; i += 2)
        checked_prime_flag[i] = true;
    
    for (i = 3; i < n; i += 2)
    {
        if (checked_prime_flag[i] == false)
        {
            checked_prime_flag[i] = true;
            count++;
            for (j = i + i; j < n; j += i)
                if (checked_prime_flag[j] == false)
                    checked_prime_flag[j] = true;
        }
    }

    free(checked_prime_flag);
    return count;
}

int loop_main(char* arg)
{
    replace(arg, "[", "");
    replace(arg, "]", "");
    replace(arg, "\n", "");

    int n = atoi(arg);
    printf("n = %d\n", n);

    clock_t time_start = clock();
    int result = countPrimes(n);
    clock_t time_end = clock();

    // result print.
    printf("result = %d\n", result);
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