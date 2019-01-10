using System;

public class Solution
{
    public int Fib(int N)
    {
        if (N == 0)
            return 0;
        if (N == 1)
            return 1;
        int f_n2 = 0, f_n1 = 1, f_n0 = 0;
        for (int i = 1;  i < N; ++i)
        {
            f_n2 = f_n1 + f_n0;
            f_n0 = f_n1;
            f_n1 = f_n2;
        }
        return f_n2;
    }

    public void Main(string args)
    {
        int N = int.Parse(args.Replace("[","").Replace("]","").Trim());
        Console.WriteLine("N = " + N.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int results = Fib(N);
        Console.WriteLine("result = " + results.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
