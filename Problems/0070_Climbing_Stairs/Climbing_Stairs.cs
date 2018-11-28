using System;

public class Solution
{
    public int ClimbingStairs(int n)
    {
        if (n == 1)
            return 1;
        if (n == 2)
            return 2;
        if (n == 3)
            return 3;
        if (n == 4)
            return 5;
        
        int sum = 5;
        for (int i = 5; i <= n; i++) {
            sum = sum + (i - 2);
        }

        return sum;
    }

    /*
    1    1    1=1
    2    2    1=(1+1)
            1=(2)
    3    3    1=(1+1+1)
            2=(1+2)+(2+1)
    4    5    1=(1+1+1+1)
            3=(2+1+1)+(1+2+1)+(1+1+2)
            1=(2+2)
    5   8    1=(1+1+1+1+1)
            4=(2+1+1+1)+(1+2+1+1)+(1+1+2+1)+(1+1+1+2)
            2=(2+2+1)+(2+1+2)
            1=(1+2+2)
    6   13    1=(1+1+1+1+1+1)
            5=(2+1+1+1+1)+(1+2+1+1+1)+(1+1+2+1+1)+(1+1+1+2+1)+(1+1+1+1+2)
            3=(2+2+1+1)+(2+1+2+1)+(2+1+1+2)
            2=(1+2+1+2)+(1+1+2+2)
            1=(2+2+2)
     */

    public void Main(string args)
    {
        Console.WriteLine("n = " + args );

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();

        sw.Start();

        int ret = ClimbingStairs(int.Parse(args));
        Console.WriteLine("Result = " + ret.ToString() );
        
        sw.Stop();

        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
