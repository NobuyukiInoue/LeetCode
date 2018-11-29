using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public bool ContainsDuplicate(int[] nums)
    {
        int[] result = nums.Distinct().ToArray();
        return (result.Length != nums.Length);
    }

    public bool ContainsDuplicate2(int[] nums)
    {
        return nums.Length == nums.Distinct().Count() ? false : true;
    }

    public bool ContainsDuplicate_old(int[] nums)
    {
        int i, j;

        for (i = 0; i < nums.Length; ++i) {
            for (j = 0; j < nums.Length; ++j) {
                if (j == i)
                    continue;
                if (nums[i] == nums[j])
                    return true;
            }
        }

        return false;
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

        Console.WriteLine("Result = " + ContainsDuplicate(nums));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
