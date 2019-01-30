using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public IList<int> FindAnagrams(string s, string p)
    {
        var n = p.Length;
        var c = new int[26];
        for (int i = 0; i < n; i++)
            c[p[i] - 'a']++;

        int v = n;
        var kpath = new List<int>();
        for (int i = 0; i < s.Length; i++)
        {
            if (c[s[i] - 'a'] > 0) v--;
            c[s[i] - 'a']--;

            if (i >= n)
            {
                c[s[i - n] - 'a']++;
                if (c[s[i - n] - 'a'] > 0) v++;
            }

            if (v == 0)
                kpath.Add(i - n + 1);
        }
        return kpath;
    }

    public IList<int> FindAnagrams2(string s, string p)
    {
        IList<int> resultArray = new List<int>();

        if (s.Length < p.Length)
            return resultArray;
        
        int[] p_char_count = new int[0x80];
        int[] s_char_count = new int[0x80];

        int i;
        for (i = 0; i < p.Length; ++i) {
            p_char_count[p[i]]++;
        //  Console.WriteLine("p_char_count[" + p[i] + "] = " + p_char_count[p[i]]);
        }
        for (i = 0; i < p.Length - 1; ++i) {
            s_char_count[s[i]]++;
        //   Console.WriteLine("s_char_count[" + s[i] + "] = " + s_char_count[s[i]]);
        }
        for (i = p.Length - 1; i < s.Length; ++i)
        {
        //  Console.WriteLine("s_char_count[" + s[i] + "] = " + s_char_count[s[i]]);
            s_char_count[s[i]]++;
            if (i - p.Length >= 0)
            {
                s_char_count[s[i - p.Length]]--;
            }
            if (diff_char_count(s_char_count, p_char_count)) {
                resultArray.Add(i - p.Length + 1);
            }
        }

        return resultArray;
    }

    public bool diff_char_count(int[] p_char_count, int[] s_char_count)
    {
        for (int i = 0; i < p_char_count.Length; ++i) {
            if (p_char_count[i] != s_char_count[i]) {
            //  Console.WriteLine("p_char_count[" + Convert.ToChar(i) + "] = " + p_char_count[i] + ", s_char_count[" + Convert.ToChar(i) + "] = " + s_char_count[i]);
                return false;
            }
        }
        return true;
    }

    public string output_IList(IList<int> arr)
    {
        if (arr.Count <= 0)
            return "[]";

        string resultStr = "[" + arr[0];

        for (int i = 1; i < arr.Count; ++i)
            resultStr += "," + arr[i];

        resultStr += "]";

        return resultStr;
    }

    public void Main(string args)
    {
        string var_str = args.Replace("\"","").Replace("[","").Replace("]","").Trim();
        string[] flds = var_str.Split(',');
        string s = flds[0];
        string p = flds[1];

        Console.WriteLine("s = " + s + ", p = " + p);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        IList<int> result = FindAnagrams(s, p);
        Console.WriteLine("result = " + output_IList(result));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
        /*
        Console.Write("Hit Any Key");
        Console.Read();
        */
    }
}
