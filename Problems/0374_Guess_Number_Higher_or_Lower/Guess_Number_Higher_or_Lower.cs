using System;
using System.Collections.Generic;

public class Solution {
    public int guessNumber(int n)
    {
        int low = 1, high = n, mid;
        while(low <= high) {
            mid = low + (high - low)/2;
            if(guess(mid) == -1) {
                high = mid - 1;
            }
            else if(guess(mid) == 1) {
                low = mid + 1;
            }
            else {
                return mid;
            }
        }
        return 0;
    }

    public int guess(int n)
    {
        if (n > 6)
            return -1;
        else if (n < 6)
            return 1;
        else
            return 0;
    }

    public void Main(string args)
    {
        int n = int.Parse(args);

        Console.WriteLine("num = " + n.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();
        
        int result = guessNumber(n);

        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
