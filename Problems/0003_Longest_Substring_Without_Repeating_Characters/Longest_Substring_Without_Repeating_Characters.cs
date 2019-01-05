using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public int LengthOfLongestSubstring(string s)
    {     
        int largestLength = 0, currLength = 1, start = 0;
        
        for (int i = 0; i < s.Length; ++i, ++currLength) 
        {
            int found = s.Substring(start, currLength).IndexOf(s[i]);
            if (found != (i - start) && found != -1)
            {
                int subtractionLength = found + 1;
                currLength = currLength - subtractionLength;
                start += subtractionLength;
            }
            
            if (currLength > largestLength)
            {
                largestLength = currLength;
            }
        }
        
        return largestLength;
    }

    public void Main(string args)
    {
        string s = args.Replace("\"","").Replace("[","").Replace("]","").Trim();

        Console.WriteLine("s = " + s);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = LengthOfLongestSubstring(s);
        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
