using System;
using System.Collections.Generic;

public class Solution
{
    public bool IsAnagram(string s, string t)
    {
        if (s == null || t == null)
            return false;
        if (s.Length != t.Length)
            return false;
        
        Dictionary<char, int> dic_st = new Dictionary<char, int>();

        foreach (char char_s in s)
            if (dic_st.ContainsKey(char_s))
                dic_st[char_s]++;
            else
                dic_st.Add(char_s, 1);

        foreach (char char_t in t)
            if (dic_st.ContainsKey(char_t))
            {
                if (dic_st[char_t] == 0)
                    return false;
                dic_st[char_t]--;
            }
            else
                return false;

        return true;        
    }

    public bool IsAnagram_char(string s, string t)
    {
        if (s == null || t == null)
            return false;
        if (s.Length != t.Length)
            return false;

        char[] array_s = s.ToCharArray();
        char[] array_t = t.ToCharArray();

        Array.Sort(array_s);
        Array.Sort(array_t);
        
        Dictionary<char, int> dic_st = new Dictionary<char, int>();

        foreach (char char_s in array_s)
            if (dic_st.ContainsKey(char_s))
                dic_st[char_s]++;
            else
                dic_st.Add(char_s, 1);

        foreach (char char_t in array_t)
            if (dic_st.ContainsKey(char_t))
            {
                if (dic_st[char_t] == 0)
                    return false;
                dic_st[char_t]--;
            }
            else
                return false;

        return true;
    }

    public string output_str_array(string[] words)
    {
        if (words.Length <= 0)
            return "";
        
        string results = words[0];
        for (int i = 1; i < words.Length; ++i)
        {
            results += ", " + words[i];
        }

        return results;
    }

    public void Main(string args)
    {
        string[] words = args.Replace("\"","").Replace(" ","").Replace("[","").Replace("]","").Trim().Split(',');
        string s = null;
        string t = null;

        if (words.Length >= 2)
        {
            s = words[0];
            t = words[1];
        }

        Console.WriteLine("s = " + s);
        Console.WriteLine("t = " + t);
        
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        bool result = IsAnagram(s, t);
        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
