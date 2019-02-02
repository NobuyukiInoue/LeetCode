using System;
using System.Collections.Generic;
using System.Linq;

public class Program
{
    public void Main()
    {
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();

        Console.WriteLine("Hit Return Key...");
        sw.Start();

        Console.ReadLine();
        sw.Stop();

        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
