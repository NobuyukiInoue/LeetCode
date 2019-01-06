using System;
using System.IO;

namespace Project_CS
{
    public class Solution
    {
        public int ClimbingStairs(int n)
        {
            int[] results = new int[n + 1];
            results[0] = 0;
            if (n > 0)
                results[1] = 1;
            if (n > 1)
                results[2] = 2;
            for (int i = 3; i <= n; ++i)
            {
                results[i] = results[i - 1] + results[i - 2];
            }

            return results[n];
        }

        public void Main(string args)
        {
            int n = int.Parse(args);
            Console.WriteLine("n = " + n.ToString() );

            System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();

            sw.Start();

            int result = ClimbingStairs(n);
            Console.WriteLine("Result = " + result.ToString() );
            
            sw.Stop();

            Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
           if (args.Length < 1)
            {
                Console.WriteLine("Usage: dotnet run Program <testdata.txt>");
                return;
            }

            if (System.IO.File.Exists(args[0]) == false)
            {
                Console.WriteLine(args[0] + "not found.");
                return;
            }

            Solution sl = new Solution();
            StreamReader sr = new StreamReader(args[0]);
            string line;

            while ((line = sr.ReadLine()) != null)
            {
                sl.Main(line);
            }

            sr.Close();
            sl = null;
        }
    }
}
