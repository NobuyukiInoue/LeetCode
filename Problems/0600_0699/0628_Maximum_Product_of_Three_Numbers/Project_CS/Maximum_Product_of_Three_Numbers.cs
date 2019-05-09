using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public int MaximumProduct(int[] nums)
    {
        int max1 = int.MinValue, max2 = int.MinValue, max3 = int.MinValue, min1 = int.MaxValue, min2 = int.MaxValue;
        foreach (int n in  nums)
        {
            if (n > max1) {
                max3 = max2;
                max2 = max1;
                max1 = n;
            } else if (n > max2) {
                max3 = max2;
                max2 = n;
            } else if (n > max3) {
                max3 = n;
            }

            if (n < min1) {
                min2 = min1;
                min1 = n;
            } else if (n < min2) {
                min2 = n;
            }
        }

        return Math.Max(max1*max2*max3, max1*min1*min2);
    }

    public int MaximumProduct2(int[] nums)
    {
        Array.Sort(nums);
        int a = nums[nums.Length - 1] * nums[nums.Length - 2] * nums[nums.Length - 3];
        int b = nums[0] * nums[1] * nums[nums.Length - 1];
        if (a > b)
            return a;
        else
            return b;
    }

    public int[] str_to_int_array(string s)
    {
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
        string flds = args.Replace("[","").Replace("]","").Trim();
        int[] nums = str_to_int_array(flds);
    	Console.WriteLine("nums = " + output_int_array(nums));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = MaximumProduct(nums);
        Console.WriteLine("result = " + result.ToString());

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
