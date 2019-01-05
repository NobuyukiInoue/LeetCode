using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public bool IsMatch(string s, string p)
    {
    
    }
    public void Main(string args)
    {
        string[] flds = args.Replace("\"","").Replace("[","").Replace("]","").Trim().Split(',');
        string s = flds[0];
        string p = flds[1];

        Console.WriteLine("s = " + s + ", p = " + p);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        bool result = IsMatch(s, p);
        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
