using System;
using System.Collections.Generic;

public class Solution {
    public bool IsPerfectSquare(int num)
    {
        int high = 46340, low = 0, mid;

        while (low <= high) {
            mid = low + (high - low)/2;
            if (mid*mid > num) {
                high = mid - 1;
            }
            else if (mid*mid < num) {
                low = mid + 1;
            }
            else {
                return true;
            }
        }
        return false;
    }

    public void Main(string args)
    {
        int num = int.Parse(args);

        Console.WriteLine("num = " + num.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();
        
        bool result = IsPerfectSquare(num);

        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
