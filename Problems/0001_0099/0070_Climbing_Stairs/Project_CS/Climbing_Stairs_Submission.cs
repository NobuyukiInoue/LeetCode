using System;

public class Solution2
{
    public int ClimbStairs(int n)
    {
        return Climb_Stairs(0, n);
    }

    public int Climb_Stairs(int i, int n)
    {
        if (i > n) {
            return 0;
        }
        if (i == n) {
            return 1;
        }

        return Climb_Stairs(i + 1, n) + Climb_Stairs(i + 2, n);
    }

    public void Main(string args)
    {
        Console.WriteLine("n = " + args );

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();

        sw.Start();

        int ret = ClimbStairs(int.Parse(args));
        Console.WriteLine("Result = " + ret.ToString() );
        
        sw.Stop();

        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
