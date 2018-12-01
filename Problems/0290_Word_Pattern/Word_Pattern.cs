using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public bool WordPattern(string pattern, string str)
    {
        string[] words = str.Split(' ');

        if (pattern.Length != words.Length)
            return false;

        int i, j;

        for (i = 0; i < pattern.Length; ++i)
            for ( j = i + 1; j < pattern.Length; ++j)
                if (pattern[i] == pattern[j])
                    if (words[i] != words[j])
                        return false;
        
        for (i = 0; i < words.Length - 1; ++i)
            for (j = i + 1; j < words.Length; ++j)
                if (words[i] == words[j])
                    if (pattern[i] != pattern[j])
                        return false;

        return true;
    }

    public void Main(string args)
    {
        string[] flds = args.Replace("\"","").Split(',');
        string pattern = flds[0];
        string var_str = flds[1];

        Console.WriteLine("pattern = " + pattern + ", str = " + var_str);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        bool result = WordPattern(pattern, var_str);

        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
