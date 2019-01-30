using System;
using System.Collections.Generic;

public class Solution
{
    public int ThreeSumClosest(int[] nums, int target)
    {
        int min = int.MaxValue;
        int result = 0;

        Array.Sort(nums);
        
        for(int i = 0; i < nums.Length - 2; i++)
        {
            int j = i + 1;
            int k = nums.Length - 1;
            while (j < k)
            {
                int sum =  nums[i] + nums[j] + nums[k];
                int diff = Math.Abs(sum - target);
                if (diff == 0) return sum;
                
                if (diff < min) {
                    min = diff;
                    result = sum;
                }
                if (sum <= target)
                    j++;
                else
                    k--;
            }
        }
        return result;
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
        string arg_str = args.Replace("[[","").Replace("]]","").Trim();
        string[] flds = arg_str.Split(new string[] {"],["}, StringSplitOptions.None);
        int[] nums = str_to_int_array(flds[0]);
        int target = int.Parse(flds[1]);

        Console.WriteLine("nums = " + output_int_array(nums));
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = ThreeSumClosest(nums, target);
        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
