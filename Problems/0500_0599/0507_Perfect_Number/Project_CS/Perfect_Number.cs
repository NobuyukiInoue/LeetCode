using System;
using System.Linq;
using System.Collections.Generic;

public class Solution
{
    public bool CheckPerfectNumber(int num)
    {
        if (num <= 1)
            return false;
        
        // Find all the positive divisors
        List<int> div = new List<int>();

        for (int i = 1; i < (int)Math.Pow(num, 0.5) + 1; ++i)
        {
            if (num % i == 0)
            {
                div.Add(i);
                div.Add(num / i);
            }
        }
        
        int sum = -num;
        for (int i = 0; i < div.Count; ++i)
            sum += div[i];

        if (sum == num)
            return true;
        else
            return false;
    }

    public void Main(string args)
    {
        int num = int.Parse(args.Replace("[","").Replace("]","").Trim());
        Console.WriteLine("num = " + num.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        bool results = CheckPerfectNumber(num);
        Console.WriteLine("result = " + results.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
