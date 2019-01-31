using System;

public class Solution
{
    public int MaxProfit(int[] prices)
    {
        int max = 0;
        int sum_max = 0;
        int min = int.MaxValue;

        for(int i = 0; i < prices.Length; i++)
        {
            if(min > prices[i])
                min = prices[i];
            if(prices[i] - min > max)
                max = prices[i] - min;
            if(prices[i] - min > 0) {
                sum_max += prices[i] - min;
                min = prices[i];
            }
        }
        
        if (max > sum_max)
            return max;
        else
            return sum_max;
    }

    public int[] str_to_int_array(string s)
    {
        if (s.Length <= 0)
            return null;

        string[] flds = s.Split(',');
        int[] nums = new int[flds.Length];

        if (flds.Length <= 0)
            return nums;

        for (int i = 0; i < nums.Length; ++i)
        {
            nums[i] = int.Parse(flds[i]);
        }

        return nums;
    }

    public string output_int_array(int[] nums)
    {
        if (nums.Length <= 0)
            return "";

        string resultStr = "[" +  nums[0].ToString();
 
        for (int i = 1; i < nums.Length; ++i)
        {
            resultStr += "," + nums[i].ToString();
        }

        return resultStr + "]";
    }

    public void Main(string args)
    {
        string flds = args.Replace("\"", "").Replace(" ", "").Replace("[", "").Replace("]", "");
        int[] prices = str_to_int_array(flds);
        Console.WriteLine("prices[] = " + output_int_array(prices));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = MaxProfit(prices);

        sw.Stop();
        Console.WriteLine("Result = " + result.ToString());
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
