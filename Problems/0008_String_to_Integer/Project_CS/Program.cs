using System;
using System.IO;

namespace Project_CS
{
    public class Solution
    {
        public int MyAtoi(string str)
        {
            str = str.Trim();
            bool neg = false;
            long x = 0;
            for(var i =0; i <str.Length;++i)
            {
                if (i==0 && str[0] == '-')
                {
                    neg = true;
                    continue;
                }
                if (i==0 && str[0] == '+')
                {                   
                    continue;
                }
                if (str[i] < '0' || str[i] > '9')
                {
                    break;
                }
                x = x * 10 + (str[i] - '0');
                if (x > int.MaxValue)
                {
                    return neg? int.MinValue:int.MaxValue;
                }
            }

            return neg? -1 * (int)x: (int) x;
        }

        public int MyAtoi_work(string str)
        {
            string workStr = str.Trim();

            if (workStr.IndexOf("+-") >= 0 || workStr.IndexOf("-+") >= 0)
                return 0;

            if (workStr.IndexOf('+') == 0)
            {
                workStr = workStr.Substring(1);
            }

            bool isPositive = true;
            if (workStr.IndexOf('-') == 0)
            {
                workStr = workStr.Substring(1);
                isPositive = false;
            }

            int result = 0;
            for (int i = 0; i < workStr.Length; ++i)
            {
                if (workStr[i] >= '0' && workStr[i] <= '9')
                {
                    try
                    {
                        checked
                        {
                            result *= 10;
                            result += (int)workStr[i] - '0';
                        }
                    }
                    catch(OverflowException ex)
                    {
                        if (isPositive)
                            return int.MaxValue;
                        else
                            return int.MinValue;
                    }
                }
                else if (i == 0)
                    return 0;
                else
                    break;
            }

            if (isPositive)
                return result;
            else
                return -result;
        }

        public void Main(string args)
        {
            //string str = args.Replace("\"","").Replace("[","").Replace("]","").Trim();
            string str = args.Replace("\"","").Replace("[","").Replace("]","").Replace("\n","");

            Console.WriteLine("str = " + str);

            System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
            sw.Start();

            int result = MyAtoi(str);
            Console.WriteLine("result = " + result.ToString());
            
            sw.Stop();
            Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
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
