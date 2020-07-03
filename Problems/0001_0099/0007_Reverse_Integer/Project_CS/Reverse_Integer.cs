using System;

public class Solution {
    static public int Reverse1(int x)
    {
        int rev = 0;
        while (x != 0)
        {
            int pop = x % 10;
            x /= 10;
            if (rev > int.MaxValue/10 || (rev == int.MaxValue / 10 && pop > 7))
                return 0;
            if (rev < int.MinValue/10 || (rev == int.MinValue / 10 && pop < -8))
                return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }

    public int Reverse(int x)
    {
        int rev = 0;
        try
        {
            while (x != 0)
            {
                rev = checked((rev * 10) + (x % 10));
                x = x / 10;
            }
        }
        catch
        {
            return 0;
        }

        return rev; 
    }

    static public int Reverse3(int x)
    {
        string temp = "";
        int val = Math.Abs(x);

        if (val < 0)
            temp = "-";

        do {
            temp += (val % 10).ToString();
            val = val / 10;
        } while ( val > 0);

        return int.Parse(temp);
    }

    public void Main(string args)
    {
        string fld = args.Replace("[","").Replace("]","").Trim();
        int x = int.Parse(fld);

        Console.WriteLine("x = " + x.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();
        
        int result = Reverse(x);

        Console.WriteLine("result = " + result);

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
