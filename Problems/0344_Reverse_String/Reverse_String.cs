using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    /*
    public string ReverseString_old1(string s)
    {
        string resultStr = String.Copy(s);
        for (int i = 0; i < s.Length; ++i)
            resultStr[i] = s[s.Length - 1 - i];
        return resultStr;
    }

    public string ReverseString_old2(string s) {
        string resulStr = "";
        for (int i = s.Length - 1; i >= 0; --i)
            resulStr += s[i];
        return resulStr;        
    }
    */

    public string ReverseString(string s)
    {
        char[] x = s.ToCharArray();
        for (int i = 0; i < s.Length; ++i) {
            x[i] = s[s.Length - 1 - i];
            x[s.Length - 1 - i] = s[i];
        }
        return new string(x);
    }

    public void Main(string args)
    {
        string var_str = args.Replace("\"","");

        Console.WriteLine("s = " + var_str);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        string result = ReverseString(var_str);

        Console.WriteLine("result = " + result);
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
