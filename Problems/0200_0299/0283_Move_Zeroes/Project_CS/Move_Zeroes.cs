using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public void MoveZeroes(int[] nums)
    {
        int[] temp = nums;

        int dst_i = 0;
        for (int src_i = 0; src_i < nums.Length; ++src_i) {
            if (temp[src_i] != 0) {
                nums[dst_i] = temp[src_i];
                dst_i++;
            }
        }

        for (int leaset_i = dst_i; leaset_i < nums.Length; ++leaset_i)
            nums[leaset_i] = 0;
        /*
        int leaset_i = dst_i;
        while (leaset_i < nums.Length)
            nums[leaset_i++] = 0;
        */
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

        MoveZeroes(nums);
        Console.WriteLine("nums = " + output_array_int(nums));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
