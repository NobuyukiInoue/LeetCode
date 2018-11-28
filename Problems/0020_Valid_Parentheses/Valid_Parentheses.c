bool isValid(char* s) {
	char stack[65535];
	int i = 0, n = 0;
	int s_len;

	s_len = strlen(s);
	
	for (i = 0; i < s_len; i++ ) {

		if ( n < 0 )
			return false;

		if ( s[i] == '(' )
			stack[n++] = s[i];
		else if ( s[i] == '{' ) 
			stack[n++] = s[i];
		else if ( s[i] == '[' )
			stack[n++] = s[i];
		else if ( n > 0 )
			if ( s[i] == ')' && stack[n - 1] == '(' )
				--n;
			else if ( s[i] == '}' && stack[n - 1] == '{' )
				--n;
			else if ( s[i] == ']' && stack[n - 1] == '[' )
				--n;
			else
				return false;
		else
			return false;
	}

	if ( n == 0 )
		return true;
	else
		return false;
}
	
void main(void)
{
	printf("%\n", IsValid("{()[]}}"));
}
