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
        uint n = uint.Parse(args.Replace("[", "").Replace("]", "").Trim());

        Console.WriteLine("n = " + n.ToString());
        Console.WriteLine(Convert.ToString(n, 2).PadLeft(32, '0'));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();
        
        uint result = reverseBits(n);

        Console.WriteLine("result = " + result.ToString());
        Console.WriteLine(Convert.ToString(result, 2).PadLeft(32, '0'));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
