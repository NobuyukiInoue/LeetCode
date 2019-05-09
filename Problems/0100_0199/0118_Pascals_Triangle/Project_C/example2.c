#include <stdio.h>
#include <stdlib.h>

void main(void)
{
//  int *data[] = { {1}, {2, 2}, {3, 3, 3} };
    int *data[3];
    int data_length;

    data[0] = (int *)malloc(1 * sizeof(int));
    data[1] = (int *)malloc(2 * sizeof(int));
    data[2] = (int *)malloc(3 * sizeof(int));

    data[0][0] = 1;

    data[1][0] = 2;
    data[1][1] = 2;

    data[2][0] = 3;
    data[2][1] = 3;
    data[2][2] = 3;

    data_length = sizeof(data) / sizeof(char *);
    printf("data_length = %d\n", data_length);

    /*
    for (int i = 0; i < data_length; ++i) {
        for(int j = 0; j < sizeof(data[i]); ++j) {  // Bug!!! ///
            printf("data[%d]_length = %d\n", i, sizeof(data[i]);
            printf("data[%d][%d] = %d\n", i, j, data[i][j]);
        }
    }
    */

    for (int i = 0; i < data_length; ++i) {
        for(int j = 0; j < i + 1; ++j) {
            printf("data[%d][%d] = %d\n", i, j, data[i][j]);
        }
    }
}
