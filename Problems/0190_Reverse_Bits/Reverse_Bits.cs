using System;
using System.Collections.Generic;

public class Solution {
    public uint reverseBits(uint n)
    {
        uint result = 0;
        for (int i = 0; i < 32; ++i) {
            result = result*2 + n%2;
            n /= 2;
        }
        
        return result;
    }

    public void Main(string args)
    {
        uint n = uint.Parse(args);

        Console.WriteLine("n = " + n.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();
        
        uint result = reverseBits(n);

        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
