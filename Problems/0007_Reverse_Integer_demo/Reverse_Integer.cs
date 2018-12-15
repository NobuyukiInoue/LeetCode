using System;

public class Solution {
    static public int Reverse(int x)
    {
        int rev = 0;
        while (x != 0)
        {
            int pop = x % 10;
            x /= 10;
            if (rev > int.MaxValue/10 || (rev == int.MaxValue / 10 && pop > 7))  return 0;
            if (rev < int.MinValue/10 || (rev == int.MinValue / 10 && pop < -8)) return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }

    public void Main(string args)
    {
        int x = int.Parse(args);

        Console.WriteLine("x = " + x.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();
        
        Console.WriteLine("result = " + Reverse(x).ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
