using System;
using System.Collections.Generic;

public class Solution {
    public char FindTheDifference(string s, string t)
    {
        int sum = t[0];

        for(int i = 1; i < t.Length; i++)
            sum = sum + t[i] - s[i - 1];

        return (char)sum;
    }

    public char FindTheDifference_old(string s, string t)
    {
        char[] str = "abcdefghijklmnopqrstuvwxyz".ToCharArray();
        
        for (int i = 0; i < str.Length; ++i) {
            if (s.Split(str[i]).Length != t.Split(str[i]).Length) {
                return str[i];
            }
        }

        return '0';
    }

    public void Main(string args)
    {
        string[] flds = args.Split(',');
        string s = flds[0];
        string t = flds[1];

        Console.WriteLine("s = " + s + ", t = " + t);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();
        
        char result = FindTheDifference(s, t);

        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
