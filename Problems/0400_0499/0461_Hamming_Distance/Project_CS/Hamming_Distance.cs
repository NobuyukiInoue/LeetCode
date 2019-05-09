using System;
using System.Linq;

public class Solution
{
    public int HammingDistance(int x, int y)
    {
        int z = x ^ y;
        int counts = 0;
        for ( ;z > 0; z /= 2)
        {
            if (z % 2 == 1)
            {
                counts++;
            }
        }

        return counts;
    }

    public int HammingDistance2(int x, int y)
    {
        int xor = x ^ y;
        int distance = 0;
        while (xor > 0)
        {
            distance += xor & 1;
            xor = xor >> 1;
        }
        return distance;
    }

    public void Main(string args)
    {
        string[] flds = args.Replace("[","").Replace("]","").Trim().Split(',');
        int x = int.Parse(flds[0]);
        int y = int.Parse(flds[1]);

        Console.WriteLine("x = " + x.ToString() + ", y = " + y.ToString());
        
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = HammingDistance(x, y);
        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
