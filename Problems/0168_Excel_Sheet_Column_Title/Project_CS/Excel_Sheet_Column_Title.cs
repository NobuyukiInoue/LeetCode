using System;
using System.Collections.Generic;

public class Solution {
    public string ConvertToTitle(int n)
    {
        if (n < 1)
            return "";

        int temp = n - 1;
        var target = new List<int>();
        int mod, count = 0;

        while (true) {
            mod = temp % 26;
            target.Add(mod);
            count++;
            temp -= mod;
            if (temp >= 26) {
                temp = (int)(temp / 26) - 1;
                continue;
            }
            else
                break;
        }
            
        string result = "";

        for (int i = 0; i < count; ++i)
            result = (char)((int)'A' + target[i]) + result;

        return result;
    }

    public void Main(string args)
    {
        string temp = args.Replace(" ", "").Replace("[", "").Replace("]", "").Trim();
        int n = int.Parse(temp);
        Console.WriteLine("n = " + n.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        String result = ConvertToTitle(n);

        sw.Stop();
        Console.WriteLine("Result = " + result);
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
