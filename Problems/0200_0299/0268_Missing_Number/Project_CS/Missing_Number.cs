using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public int MissingNumber(int[] nums)
    {
        bool[] checked_flag = new bool[nums.Length + 1];
        int i;

        for (i = 0; i < nums.Length; ++i)
            checked_flag[nums[i]] = true;
        
        for (i = 0; i < checked_flag.Length; ++i)
            if (checked_flag[i] == false)
                return i;
        
        return i;
    }

    private int[] set_array_int(string[] flds)
    {
        if (flds.Length == 0)
            return null;
        
        int[] nums = new int[flds.Length];
        for (int i = 0; i < flds.Length; ++i)
            nums[i] = int.Parse(flds[i]);

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
        string[] flds = args.Replace("[","").Replace("]","").Split(',');
        int[] nums = set_array_int(flds);
        Console.WriteLine("nums = " + output_array_int(nums));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        Console.WriteLine("Result = " + MissingNumber(nums));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
