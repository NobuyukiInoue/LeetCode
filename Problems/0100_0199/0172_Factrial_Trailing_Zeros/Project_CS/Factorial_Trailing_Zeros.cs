using System;
using System.Collections.Generic;

public class Solution {

    public int TrailingZeroes(int n)
    {
        int x = 5, result = 0;
        while (n >= x) {
            result += n/x;
            if ( x <= int.MaxValue/2 ) {
                x *= 5;
            }
            else
                break;
        } 
        
        return result;
    }

    public int TrailingZeroes_work(int n)
    {
        ulong trailingNum = 1;
        for (int i = n; i >= 1; --i) {
            trailingNum *= (ulong)i;
        }

        Console.WriteLine("trailingNum = " + trailingNum.ToString());
        ulong x = 10;
        int count = 0;

        while (x < trailingNum)
            if (trailingNum % x == 0) {
                count++;
                x *= 10;
            }
            else 
                return count;

        return count;
    }

    public void Main(string args)
    {
        string temp = args.Replace(" ", "").Replace("[", "").Replace("]", "").Trim();
        int n = int.Parse(temp);
    	Console.WriteLine("n = " + n.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = TrailingZeroes(n);

        Console.WriteLine("result = " + result.ToString());

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
