using System;
using System.Collections.Generic;

public class Solution
{
    public int[] TwoSum(int[] nums, int target)
    {
        Dictionary<int, int> ValuesMap = new Dictionary<int,int>();
       
        for(int i = 0, len = nums.Length; i < len; i++)
        {
            var rem = target - nums[i];

            //check if rem exists.
            if (ValuesMap.ContainsKey(rem))
            {
                return new int[]{ValuesMap[rem],i};
            } else {
                ValuesMap[nums[i]] = i;
            }
        }
        return new int[0];
    }

    public int[] TwoSum_work(int[] nums, int target)
    {
        for (int i = 0; i < nums.Length; i++)
        {
            for (int j = i + 1; j < nums.Length; j++)
            {
                if (nums[i] + nums[j] == target ){
                    return (new int[2] {i, j});
                }
            }
        }
        
        return (new int[2] {0, 0});
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
        int target = int.Parse(flds[1]);

        Console.WriteLine("nums = " + output_int_array(nums));
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int[] result = TwoSum(nums, target);
        Console.WriteLine("result = " + output_int_array(result));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
