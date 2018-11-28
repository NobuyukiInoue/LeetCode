using System;
using System.Collections.Generic;

public class Solution {
    public bool IsHappy(int n)
    {
        int temp = n;
        List<int> flds = new List<int>();

        while (true){
            do {
                flds.Add(temp % 10);
                temp /= 10;
            } while (temp > 0);

            temp = 0;
            for (int i = 0; i < flds.Count; ++i) {
                temp += (int)Math.Pow(flds[i], 2);
            }

            if (temp == 1)
                return true;
            if (temp == 2)
                return false;
            if (temp == 3)
                return false;
            if (temp == 4)
                return false;
            if (temp == 5)
                return false;
            flds.Clear();
        }
    }

    public void Main(string args)
    {
        int n = int.Parse(args);

        Console.WriteLine("n = " + n.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();
        
        bool result = IsHappy(n);

        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
