using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public int FirstUniqChar(string s)
    {
        return s.IndexOf(s.GroupBy(x => x).Where(g => g.Count() == 1).Select(x => x.Key).FirstOrDefault());
    }
    
    public int FirstUniqChar_work(string s)
    {
        if (s.Length <= 1)
            return s.Length - 1;
        
        bool[] checkedList = new bool[s.Length];
        int i, j;
        for (i = 0; i < s.Length - 1; ++i) {
            if (checkedList[i])
                continue;
            for (j = i + 1; j < s.Length; ++j) {
                if (s[i] == s[j]){
                    checkedList[i] = true;
                    checkedList[j] = true;
                }
            }
        }

        for (i = 0; i < s.Length; ++i)
            if (checkedList[i] == false)
                return i;

        return -1;
    }

    public void Main(string args)
    {
        string var_str = args.Replace("\"","");

        Console.WriteLine("s = " + var_str);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = FirstUniqChar(var_str);
        Console.WriteLine("result = " + result);
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
