using System;

public class Solution
{
    public int Divide(int dividend, int divisor)
    {
       if(divisor == 0 | (dividend  == Int32.MinValue && divisor == -1))
           return Int32.MaxValue;
        
        bool sign = (dividend > 0)^(divisor>0);
        uint dd = (uint)(dividend < 0 ? -dividend : dividend);
        uint dr = (uint)(divisor < 0? -divisor : divisor);
        int reminder = 0;
        
        for (int i = 31; i >= 0; i--)
        {
            if ((dd >> i) >= dr)
            {
                reminder = reminder << 1 | 0x01;
                dd -= dr << i;
            } else
                reminder = reminder << 1;
        }
        return sign? -reminder : reminder;
    }

    public int Divide_work(int dividend, int divisor)
    {
        int result = 0, isPositive;

        if (dividend*divisor >= 0) 
            isPositive = 1;
        else
            isPositive = -1;

        dividend = Math.Abs(dividend);
        divisor = Math.Abs(divisor);
        int[] div_list = new int[6];
        div_list[0] = divisor*100000;
        div_list[1] = divisor*10000;
        div_list[2] = divisor*1000;
        div_list[3] = divisor*100;
        div_list[4] = divisor*10;
        div_list[5] = divisor;

        foreach (int temp in div_list)
        {
            while (dividend - temp >= 0)
            {
                dividend -= temp;
                result += (temp / divisor);
            }
        }

        result *= isPositive;

        if (result < int.MinValue)
            return int.MinValue;
        else if (result > int.MaxValue)
            return int.MaxValue;
        else
            return result;
    }

    public void Main(string args)
    {
        string[] arg_str = args.Replace("[","").Replace("]","").Trim().Split(',');
        int dividend = int.Parse(arg_str[0]);
        int divisor = int.Parse(arg_str[1]);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = Divide(dividend, divisor);
        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
