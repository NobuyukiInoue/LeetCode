using System;

public class Solution
{
    public int PoorPigs(int buckets, int minutesToDie, int minutesToTest)
    {
        int pigs = 0;
        while (checked(Math.Pow(minutesToTest / minutesToDie + 1, pigs)) < buckets)
            pigs++;
        return pigs;
    }

    public void Main(string args)
    {
        string[] flds = args.Replace("[","").Replace("]","").Trim().Split(',');
        int buckets = int.Parse(flds[0]);
        int minutesToDie = int.Parse(flds[1]);
        int minutesToTest = int.Parse(flds[2]);

        if (minutesToDie > minutesToTest)
        {
            Console.WriteLine("minutesToTest is lower than minutesToTest.");
            return;
        }

        Console.WriteLine("buckets = " + buckets.ToString() + ", minutesToDie = " + minutesToDie.ToString() + ", minutesToTest = " + minutesToTest.ToString());
        
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = PoorPigs(buckets, minutesToDie, minutesToTest);
        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
