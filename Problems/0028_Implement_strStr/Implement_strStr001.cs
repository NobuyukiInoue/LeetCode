using System;

public class Solution {
	public int StrStr(string haystack, string needle)
	{
		return(haystack.IndexOf(needle));
	}

	public void Main()
	{
		Console.Write( StrStr("hello", "ll") );
	}
}
