#include <stdio.h>

int searchInsert(int* nums, int numsSize, int target)
{
	int i;
	
	for ( i = 0; i < numsSize; i++ ) {
		if ( nums[i] < target ) {
			continue;
		}
		else if ( nums[i] >= target ) {
			return i;
		}
	}
	
	return i;
}


void main(void)
{
	int data[] = { 1, 3, 5, 6 };
	printf("%d\n", searchInsert(data, 4, 5) );
}
