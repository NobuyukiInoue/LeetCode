using System;
using System.Collections.Generic;

public class Solution
{
    public double FindMaxAverage(int[] nums, int k)
    {
        int len = nums.Length;

        if (len == 1)
            return nums[0];

        double sum = 0;
        for(int x = 0; x < k; x++)
        {
            sum += nums[x];
        }

        double maxSum = sum;
        for(int i = 1; i <= len - k; i++)
        {
            sum = sum - nums[i - 1] + nums[i + k - 1];
            if (sum > maxSum)
                maxSum = sum;
        }
        
        return maxSum/k;
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
        string arg_str = args.Replace("[[","").Replace("]]","").Trim();
        string[] flds = arg_str.Split(new string[] {"],["}, StringSplitOptions.None);
        int[] nums = str_to_int_array(flds[0]);
        int k = int.Parse(flds[1]);

        Console.WriteLine("nums = " + output_int_array(nums) + ", k = " + k.ToString());
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        double result = FindMaxAverage(nums, k);
        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
