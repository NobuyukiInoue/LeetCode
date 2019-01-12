using System;
using System.Collections.Generic;

public class Solution
{
    public int FindPairs(int[] nums, int k)
    {
        if (k < 0)
            return 0;
        if (k == 0)
        {
            int[] sorted_nums = new int[nums.Length];
            Array.Copy(nums, sorted_nums, nums.Length);
            Array.Sort(sorted_nums);
            IList<int> outd = new List<int>();
            int prev = int.MaxValue;
            foreach (int element in sorted_nums)
            {
                if (element != prev)
                {
                    prev = element;
                    continue;
                }
                bool hit = false;
                for (int j = 0; j < outd.Count; ++j)
                {
                    if (element == outd[j])
                    {
                        hit = true;
                        break;
                    }
                }
                if (hit)
                    continue;
                outd.Add(element);
            }

            return outd.Count;
        }

        int count = 0;
        Array.Sort(nums);
        int pre_num_i, pre_num_j;
        pre_num_i = pre_num_j = int.MaxValue;

        for (int i = 0; i < nums.Length; ++i)
        {
            if (nums[i] == pre_num_i)
                continue;
            pre_num_i = nums[i];
            pre_num_j = int.MaxValue;
            for (int j = i + 1; j < nums.Length; ++j)
            {
                if (nums[j] == pre_num_j)
                    continue;
                pre_num_j = j;
                if (Math.Abs(nums[i] - nums[j]) == k)
                    count++;
            }
        }

        return count;        
    }

    public int[] str_to_int_array(string flds)
    {
        string[] data = flds.Split(',');
        if (data.Length <= 0)
            return (new int[] {});

        int[] nums = new int[data.Length];
        for (int i = 0; i < data.Length; ++i)
        {
            nums[i] = int.Parse(data[i]);
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
        string[] flds = args.Replace("[[","").Replace("]]","").Trim().Split("],[", StringSplitOptions.None);
        int[] nums = str_to_int_array(flds[0]);
        int k = int.Parse(flds[1]);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = FindPairs(nums, k);
        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
