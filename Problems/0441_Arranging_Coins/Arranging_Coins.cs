using System;
using System.Collections.Generic;

public class Solution {

    public int ArrangeCoins(int n)
    {
        if (n == 0)
            return 0;
        var res = (int)(-0.5 + 2 * Math.Sqrt(0.0625 + n / 2));       
        int temp = res + 1;

        if (((temp % 2 == 0) && (n == (temp + 1) * (temp / 2))) ||
            ((temp % 2 == 1) && (n == temp * ((temp + 1) / 2))))
            return temp;
        return res;
    }

    public int ArrangeCoins2(int n)
    {
        int row = 1;

        while (row <= n) {
            n -= row;
            row++;
        }

        return row - 1;
    }

    public void Main(string args)
    {
        int n = int.Parse(args);

        Console.WriteLine("n = " + n.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();
        
        int result = ArrangeCoins(n);

        Console.WriteLine("result = " + result);
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
