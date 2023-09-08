using System;

public class Solution
{
    public int MaxProfit(int[] prices)
    {
        // 77ms - 82ms
        int profit = 0;
        for (int i = 1; i < prices.Length; i++)
        {
            if (prices[i] > prices[i - 1])
            {
                profit += prices[i] - prices[i - 1];
            }
        }
        return profit;
    }

    public int MaxProfit2(int[] prices)
    {
        // 77ms - 86ms
        int p_max = 0;
        int p_min = int.MaxValue;
        int sum_max = 0;

        foreach (int price in prices)
        {
            p_min = Math.Min(p_min, price);
            p_max = Math.Max(p_max, price - p_min);
            if (price - p_min > 0)
            {
                sum_max += price - p_min;
                p_min = price;
            }
        }
        return p_max > sum_max ? p_max : sum_max;
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
