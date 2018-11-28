using System;
using System.Collections.Generic;

public class Solution {
    public int CountPrimes(int n)
    {
        if (n <= 2)
            return 0;
        if (n == 3)
            return 1;
        
        bool[] checked_prime_flag = new bool[n];
        int i, j, count = 1;

        for (i = 2; i < n; i += 2)
            checked_prime_flag[i] = true;
        
        for (i = 3; i < n; i += 2)
        {
            if (checked_prime_flag[i] == false)
            {
                checked_prime_flag[i] = true;
                count++;
                for (j = i + i; j < n; j += i)
                    if (checked_prime_flag[j] == false)
                        checked_prime_flag[j] = true;
            }
        }

        return count;
    }

    private string display_checked_prime_flag(bool[] checked_prime_flag)
    {
        if (checked_prime_flag.Length <= 0)
            return "";

        string resultStr = "flag[0] = " + checked_prime_flag[0].ToString() + "\n"; 

        for (int i = 1; i < checked_prime_flag.Length; i++)
        {
            resultStr += "flag[" + i.ToString() + "] = " + checked_prime_flag[i].ToString() + "\n";
        }

        return resultStr;
    }

    public void Main(string args)
    {
        int n = int.Parse(args);
        
        Console.WriteLine("n = " + n.ToString());
        
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();
        
        int result = CountPrimes(n);
        
        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
