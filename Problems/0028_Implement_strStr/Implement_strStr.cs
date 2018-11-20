using System;

public class Solution {
	public int StrStr(string haystack, string needle)
	{
		if (needle.Length == 0) {
			return 0;
		}

		if (haystack.Length == 0) {
			return -1;
		}

		int i, j, n;
		
		for ( i = 0 ; i < haystack.Length; i++ ) {
			for ( n = i, j = 0; j < needle.Length; j++, n++ ) {
				if ( n >= haystack.Length ) {
					return -1;
				}

				if ( haystack[n] != needle[j] ) {
					break;
				}
			}
			
			// Console.WriteLine("i = " + i.ToString() + ", j = " + j.ToString() );

			if ( j == needle.Length ) {
				return i;
			}
		}
	
		return -1;
	}

	public void Main()
	{
		//Console.Write( StrStr("hello", "ll") );
		//Console.Write( StrStr("aaaaa", "bba") );
		Console.Write( StrStr("mississippi", "issip") );
	}
}
