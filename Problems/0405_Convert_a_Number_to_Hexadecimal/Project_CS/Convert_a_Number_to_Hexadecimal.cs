using System;
using System.Collections.Generic;

public class Solution {
    public string ToHex(int num) {
        uint temp;

        if (num > 0)
            temp = (uint)num;
        else if (num == 0)
            return "0";
        else
            temp = (uint)Math.Pow(2,32) + (uint)num;
        //  temp = (uint)(4294967296 + num);
        
        string chars = "0123456789abcdef";
        uint modded;
        string resultStr = "";

        while (temp > 0) {
            modded = temp % 16;
            resultStr = chars[(int)modded] + resultStr;
            temp /= 16;
        }

        return resultStr;
    }

    public void Main(string args)
    {
        int num = int.Parse(args);

        Console.WriteLine("num = " + num.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();
        
        string result = ToHex(num);

        Console.WriteLine("result = " + result);
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
