using System;
using System.Collections.Generic;

public class Solution {
    public int AddDigits(int num)
    {
        if (num == 0)
            return 0;
        if (num % 9 != 0)
            return num % 9;
        else
            return 9;
    }

    public int AddDigits_work(int num)
    {
        int sum = 0, temp = num;
        do {
            do {
                sum += temp % 10;
                temp /= 10;
            } while (temp > 0);
            
            if (sum < 10)
                break;
            temp = sum;
            sum = 0;
        } while(true);

        return sum;
    }

    public void Main(string args)
    {
        int num = int.Parse(args);

        Console.WriteLine("n = " + num.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();
        
        int result = AddDigits(num);

        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
