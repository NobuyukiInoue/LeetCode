using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public bool IsMatch(string s, string p)
    {
        return IsMatch(s, p, 0, 0);
    }
    
    bool IsMatch(string s, string p, int i, int j)
    {    
        //base case - reached end of pattern
        if (j >= p.Length)
        {
            return i >= s.Length && j >= p.Length; 
        }
        
        if (j + 1 < p.Length && p[j + 1] == '*')
        {   //peek ahead for *
            while (i < s.Length && (s[i] == p[j] || p[j] == '.'))
            { 
                if (IsMatch(s, p, i, j + 2))
                    return true;
                i++;
            }
            return IsMatch(s, p, i, j + 2);
        }
        else if ( i < s.Length && ( s[i] == p[j] || p[j] == '.' ) )
        {   //direct 1-to-1 match
            return IsMatch(s, p, i + 1, j + 1);
        }
        
        return false;
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
