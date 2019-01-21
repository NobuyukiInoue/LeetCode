using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public bool RepeatedSubstringPattern(string s) {
        return (s + s).Substring(1, 2 * s.Length - 2).Contains(s);
    }

    public void Main(string args)
    {
        string s = args.Replace("\"","").Replace("[","").Replace("]","").Trim();

        Console.WriteLine("s = " + s);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        bool result = RepeatedSubstringPattern(s);
        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
