using System;

public class Solution
{
    public int MyAtoi(string str)
    {
        str = str.Trim();
        bool neg = false;
        long x = 0;
        for(var i = 0; i < str.Length; ++i)
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

    public void Main(string args)
    {
        string str = args.Replace("\"","").Replace("[","").Replace("]","").Trim();

        Console.WriteLine("str = " + str);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = MyAtoi(str);
        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
