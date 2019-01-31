using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

public class Solution
{
    public int CountSegments(string s)
    {
        if (s == null || s.Length == 0)
            return 0;

        var length = s.Length;        

        int count = 0; 
        for(int i = 0; i < length; i++)
        {
            var current = s[i];
            if (current != ' ' && (i == 0 || s[i - 1] == ' '))
                count++; 
        }

        return count; 
    }

    public int CountSegments_work(string s)
    {
        string temp = s.Trim();
        if (temp.Length == 0)
            return 0;
        while (temp.IndexOf("  ") >= 0)
            temp = temp.Replace("  ", " ");
        
        return (temp.Trim().Split(' ')).Length;
    }

    public void Main(string args)
    {
        string var_str = args.Replace("\"","");

        Console.WriteLine("s = " + var_str);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = CountSegments(var_str);

        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
