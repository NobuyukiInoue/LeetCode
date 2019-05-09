using System;
using System.Collections.Generic;

public class Solution {
    public bool IsUgly(int num) {
        if(num <= 0)
            return false;

        while(num % 2 == 0)
            num /= 2;
        while(num % 3 == 0)
            num /= 3;
        while(num % 5 == 0)
            num /= 5;
    
        return num == 1;
    }

    public void Main(string args)
    {
        int n = int.Parse(args);

        Console.WriteLine("n = " + n.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();
        
        bool result = IsUgly(n);

        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
