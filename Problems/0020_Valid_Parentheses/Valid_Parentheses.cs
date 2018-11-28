using System;

public class Solution {
    public bool IsValid(string s) {
        char[] stack = new char[s.Length];
        int n = 0;

        for (int i = 0; i < s.Length; i++ ) {

            if ( n < 0 ) {
                return false;
            }

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
    
    public void Main()
    {
        Console.Write(IsValid("{()[]}}"));
    }
}
