using System;

public class Solution {
    public string LongestCommonPrefix(string[] strs) {
    	if ( strs.Length == 0 ) {
    		return "";
    	}

    	if ( strs.Length == 1 ) {
    		return strs[0];
    	}

    	if ( strs.Length == 2 ) {
    		if ( strs[0] == strs[1] )
    			return strs[0];
    	}

    	
        int s_Len = 0;
    	int exclude_num = 0;
    	string targetStr;
    	
    	for (int n = 0; n < strs.Length; n++ ) {
    		if (strs[n].Length > s_Len) {
    			exclude_num = n;
    			s_Len = strs[n].Length;
    		}
    	}
    	
    	for (int m = s_Len; m > 0; m-- ) {
    		targetStr = strs[exclude_num].Substring(0, m);
   			if ( Check_InStr(strs, targetStr, exclude_num) )
    			return targetStr;
    	}
    	
    	return "";
    }

	public bool Check_InStr(string[] strs, string targetStr, int exclude_num)
	{
   		for (int t = 0; t < strs.Length; t++ ) {
   			if ( t == exclude_num )
   				continue;
   			if ( strs[t].IndexOf(targetStr) == 0 )
   				continue;
   			if ( strs[t].IndexOf(targetStr) < 0 )
   				return false;
   			if ( strs[t].IndexOf(targetStr) > 0 )
   				return false;
   		}
		
		return true;
	}

	public void Main()
	{
		Console.Write(LongestCommonPrefix(new string[] {"flower", "flow", "flight"}));
	}
}
