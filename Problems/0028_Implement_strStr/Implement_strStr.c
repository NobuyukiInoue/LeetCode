#include <stdio.h>

int strStr(char* haystack, char* needle) {
	if (*needle == '\0') {
		return 0;
	}

	if (*haystack == '\0') {
		return -1;
	}

	int len1, len2;
	int i, j, n;
	
	len1 = strlen(haystack);
	len2 = strlen(needle);
	
	for ( i = 0 ; i < len1; i++ ) {
		for ( n = i, j = 0; j < len2; j++, n++ ) {
			if ( n >= len1 ) {
				return -1;
			}

			if ( haystack[n] != needle[j] ) {
				break;
			}
		}

		
		if ( j == len2 ) {
			return i;
		}
	}

	return -1;
}

void main()
{
	//printf("%d\n", StrStr("hello", "ll") );
	//printf("%d\n", StrStr("aaaaa", "bba") );
	printf("%d\n", StrStr("mississippi", "issip") );
}
