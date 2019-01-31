using System;
using System.Collections.Generic;

public class Solution {
    public void Rotate(int[] nums, int k) {
        int[] temp_nums = new int[nums.Length];
        Array.Copy(nums, temp_nums, nums.Length);
        
        for (int i = 0; i < nums.Length; ++i) {
            if (i + k < nums.Length)
                nums[i + k] = temp_nums[i];
            else
                nums[(i + k) % nums.Length] = temp_nums[i];
        }
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
        string[] flds = args.Replace(" ","").Replace("[[","").Replace("]]","").Trim().Split("],[", StringSplitOptions.None);
        int[] nums = str_to_int_array(flds[0]);
        int k = int.Parse(flds[1]);

        Console.WriteLine("nus = " + output_int_array(nums) + ", k = " + k);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        Rotate(nums, k);

        sw.Stop();
        Console.WriteLine("nums(result) = " + output_int_array(nums));
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
