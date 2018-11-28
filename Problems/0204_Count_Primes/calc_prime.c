#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char *argv[])
{
	if (argc < 2) {
		printf("Usage: %s <number>\n", argv[0]);
		return 1;
	}

	int n = atoi(argv[1]);
	int i, j, k;

	printf("2");
	int count = 1;

	for(i = 3; i <= n; i += 2)
	{
		k = 0;
		for(j = 3; j <= sqrt(i); j += 2)
		{
			if(i % j == 0)
			{
				k = 1;
				break;
			}
		}

		if (k == 0) {
			printf(" %d", i);
			count++;
		}
	}

	printf("\ncount = %d\n", count);

	return 0;
}
