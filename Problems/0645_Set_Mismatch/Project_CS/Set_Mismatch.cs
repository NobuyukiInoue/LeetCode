using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public int[] FindErrorNums(int[] nums)
    {
       int len = nums.Length;
        int[] hash = new int[len];

        foreach(int item in nums)
        {
            hash[item-1]++;
        }
        int[] res = new int[2];
        for (int i = 0; i < hash.Length; ++i)
        {
            if (hash[i] == 0)
                res[1] = i + 1; 
            
            if (hash[i] > 1)
                res[0] = i + 1; 
        }
        return res;
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

    private string output_array_int(int[] nums)
    {
        if (nums.Length <= 0)
            return "";

        string resultStr = nums[0].ToString();
        for (int i = 1; i < nums.Length; ++i)
            resultStr += "," + nums[i].ToString();

        return resultStr;
    }

    public void Main(string args)
    {
        string flds = args.Replace("[","").Replace("]","");
        int[] nums = str_to_int_array(flds);
        Console.WriteLine("nums = " + output_array_int(nums));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int[] result = FindErrorNums(nums);

        sw.Stop();
        Console.WriteLine("nums = " + output_array_int(result));
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
