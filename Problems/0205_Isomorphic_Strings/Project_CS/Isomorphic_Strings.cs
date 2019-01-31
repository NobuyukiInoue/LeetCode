using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

public class Solution
{
    public bool IsIsomorphic(string s, string t)
    {
        int len = s.Length;
        var dic = new Dictionary<char, char>();
        char[] sArr = s.ToCharArray(), tArr = t.ToCharArray();
        
        for (int i = 0; i < len; i++)
        {
            if (dic.ContainsKey(sArr[i]))
            {
                if (dic[sArr[i]] != tArr[i])
                    return false;
            }
            else
            {
                if (dic.ContainsValue(tArr[i]))
                    return false;
                else
                    dic.Add(sArr[i], tArr[i]);
            }
        }
        return true;
    }

    public void Main(string args)
    {
        //string[] words = args.Replace("\"","").Replace(" ","").Replace("[","").Replace("]","").Trim().Split(',');
        string args_wrk = args.Trim();

        /*
        args_wrk = Regex.Replace(args_wrk, "^[", "");	// "["がコンパイルエラーになる。
        args_wrk = Regex.Replace(args_wrk, "]$", "");
        args_wrk = Regex.Replace(args_wrk, "^\"", "");
        args_wrk = Regex.Replace(args_wrk, "\"$", "");

        Console.WriteLine("args_wrk = " + args_wrk);
        */

        if (args_wrk.Substring(0, 2) == "[[")
            args_wrk = args_wrk.Substring(2, args_wrk.Length - 2);

        if (args_wrk.Substring(args_wrk.Length - 2, 2) == "]]")
            args_wrk = args_wrk.Substring(0, args_wrk.Length - 2);

        if (args_wrk.Substring(0, 1) == "\"")
            args_wrk = args_wrk.Substring(1);

        if (args_wrk.Substring(args_wrk.Length - 1) == "\"")
            args_wrk = args_wrk.Substring(0, args_wrk.Length - 1);

        string[] words = args_wrk.Split(new string[] {"\"],[\""}, StringSplitOptions.None);
        string s = words[0];
        string t = words[1];

        Console.WriteLine("s = " + s);
        Console.WriteLine("t = " + t);
        
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        bool result = IsIsomorphic(s, t);
        Console.WriteLine("result = " + result.ToString());
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
