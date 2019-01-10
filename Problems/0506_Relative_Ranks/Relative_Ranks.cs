using System;
using System.Linq;

public class Solution
{
    public string[] FindRelativeRanks(int[] nums)
    {
        string[] medals = new string[] {"Gold Medal", "Silver Medal", "Bronze Medal"};
        // create a sorted decending array and rank them.
        int[] ranks = new int[nums.Length];
        Array.Copy(nums,ranks, nums.Length);
        Array.Sort<int>(ranks, new Comparison<int>((i1, i2) => i2.CompareTo(i1)));
        
        string[] result = new string[nums.Length];
        for(int i = 0; i < nums.Length; ++i){
            int rank = Array.IndexOf(ranks, nums[i]);
            
            if(rank < 3)
                result[i] = medals[rank]; // return rank medal if < 3
            else    
                result[i] = (rank+1).ToString();    // return rank + 1 because index start with 0
        }
        return result;
    }

    public string[] FindRelativeRanks2(int[] nums)
    {
        string[] results = new string[nums.Length];

        if (nums.Length <= 0)
            return results;

        int[] sorted_nums = new int[nums.Length];
        Array.Copy(nums, sorted_nums, nums.Length);
        Array.Sort(sorted_nums);
        Array.Reverse(sorted_nums);

        for (int n = 0; n < results.Length; ++n)
        {
            for (int i = 0; i < sorted_nums.Length; ++i)
            {
                if (nums[n] == sorted_nums[i])
                    if (i == 0)
                        results[n] = "Gold Medal";
                    else if (i == 1)
                        results[n] = "Silver Medal";
                    else if (i == 2)
                        results[n] = "Bronze Medal";
                    else
                        results[n] = (i + 1).ToString();
            }
        }
        return results;
    }

    public int[] str_to_int_array(string[] flds)
    {
        if (flds.Length <= 0)
            return null;

        int[] nums = new int[flds.Length];
        for (int i = 0; i < nums.Length; ++i)
        {
            nums[i] = int.Parse(flds[i]);
        }

        return nums;
    }

    public string output_int_array(int[] flds)
    {
        string results = "";
        if (flds.Length <= 0)
            return results;
        
        results = flds[0].ToString();
        for (int i = 1; i < flds.Length; ++i)
        {
            results += ", " + flds[i].ToString();
        }

        return results;
    }

    public string output_str_array(string[] flds)
    {
        string results = "";
        if (flds.Length <= 0)
            return results;
        
        results = flds[0];
        for (int i = 1; i < flds.Length; ++i)
        {
            results += ", " + flds[i];
        }

        return results;
    }

    public void Main(string args)
    {
        string[] flds = args.Replace("[","").Replace("]","").Trim().Split(',');

        int[] nums = str_to_int_array(flds);
        Console.WriteLine("nums = " + output_int_array(nums));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        string[] results = FindRelativeRanks(nums);
        Console.WriteLine("result = " + output_str_array(results));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
