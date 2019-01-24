using System;
using System.IO;
using System.Numerics;

namespace Project_CS
{
    public class Solution
    {
        public int LargestPalindrome(int n)
        {
            if (n == 1)
                return 9;

            int max = (int)Math.Pow(10, n) - 1;

            for (long v = max-1; v > max/10; v--)
            {
                string str_v = v.ToString();
                char[] char_v = str_v.ToCharArray();
                Array.Reverse(char_v);
                long u = long.Parse(str_v + new string(char_v));

                for (long x = max; x*x >= u; x--)
                    if (u%x == 0)
                        return (int)(u % 1337);
            }

            return 0;
        }

        public void Main(string args)
        {
            string temp = args.Replace("[","").Replace("]","").Trim();
            int n = int.Parse(temp);
            
            System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
            sw.Start();

            int result = LargestPalindrome(n);
            Console.WriteLine("result = " + result.ToString());
            
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
                Console.WriteLine(args[0] + " not found.");
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
