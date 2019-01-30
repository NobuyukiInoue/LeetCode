using System;
using System.Collections.Generic;

public class Solution {
    public int HammingWeight(uint n)
    {
        int count = 0;
        for (int i = 0; i < 32; ++i) {
            if (n % 2 == 1)
                count++;
            n /= 2;
        }

        return count;
    }

    public void Main(string args)
    {
        uint n = uint.Parse(args);

        Console.WriteLine("n = " + n.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();
        
        int result = HammingWeight(n);

        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
