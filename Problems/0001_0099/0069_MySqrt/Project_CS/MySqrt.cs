using System;

public class Solution
{
    public int MySqrt(int x)
    {
        // 36ms
        if (x == 0)
            return 0;
        int left = 1, right = x;
        int ans = 0;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (mid <= x / mid) {
                left = mid + 1;
                ans = mid;
            } else {
                right = mid - 1;
            }
        }
        return ans;
    }

    public int MySqrt_work(int x)
    {
        int i = 1;

        while ( (uint)i*i <= x)
            i += 1000;

        i -= 1000;
        while ( (uint)i*i <= x)
            i += 100;

        i -= 100;
        while ( (uint)i*i <= x)
            i += 10;

        i -= 10;
        while ( (uint)i*i <= x)
            i++;

        return (i - 1);
    }

    public void Main(string args)
    {
        int x  = int.Parse(args.Replace("[","").Replace("]","").Trim());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();

        sw.Start();

        int result = MySqrt(x);
        Console.WriteLine("Result = " + result.ToString() );

        sw.Stop();

        Console.WriteLine("Execute time : " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
