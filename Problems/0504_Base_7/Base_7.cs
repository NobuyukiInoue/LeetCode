using System;
using System.Linq;

public class Solution
{
    public string ConvertToBase7(int num)
    {
        bool isNegative = false;

        if (num == 0)
            return "0";
        else if (num < 0)
        {
            isNegative = true;
            num = -num;
        }

        string resultStr = "";
        while (num > 0)
        {
            resultStr = (num % 7).ToString() + resultStr;
            num /= 7;
        }

        if (isNegative)
            return "-" + resultStr;
        else
            return resultStr;
    }

    public void Main(string args)
    {
        int num = int.Parse(args.Replace("[","").Replace("]","").Trim());

        Console.WriteLine("num = " + num.ToString());
        
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        string result = ConvertToBase7(num);
        Console.WriteLine("result = " + result);
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
