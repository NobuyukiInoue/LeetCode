using System;
using System.Linq;
using System.Collections;
using System.Collections.Generic;

public class Solution
{
    public List<List<int>> FourSum(int[] nums, int target)
    {
        Array.Sort(nums);
        List<List<int>> results = new List<List<int>>();
        List<int> result = new List<int>();

        findNsum(nums, target, 4, result, results);
        return results;
    }

    public void findNsum(int[] nums, int target, int N, List<int> result, List<List<int>> results)
    {
        if (nums.Length < N || N < 2)
            return;

        // solve 2-sum
        if (N == 2)
        {
            int l = 0;
            int r = nums.Length - 1;
            while (l < r)
            {
                if (nums[l] + nums[r] == target)
                {
                    result.Add(nums[l]);
                    result.Add(nums[r]);
                    results.Add(result);
                    l++;
                    r--;
                    while (l < r && nums[l] == nums[l - 1])
                        l++;
                    while (r > l && nums[r] == nums[r + 1])
                        r--;
                }
                else if (nums[l] + nums[r] < target)
                    l++;
                else
                    r--;
            }
        }
        else
        {
            for (int i = 0;  i < nums.Length - N + 1; ++i)    // careful about range
            {
                if (target < nums[i]*N || target > nums[nums.Length - 1]*N)  //take advantages of sorted list
                    break;
                if (i == 0 || i > 0 && nums[i - 1] != nums[i])  // recursively reduce N
                {
                    int[] temp = new int[nums.Length - (i + 1)];
                    Array.Copy(nums, i + 1, temp, 0, nums.Length - (i + 1));

                    List<int> result_temp = new List<int>(result);
                    result_temp.Add(nums[i]);

                    findNsum(temp, target-nums[i], N - 1, result_temp, results);
                }
            }
        }

        return;
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

    public string output_IList_array(List<List<int>> flds)
    {
        string results = "";
        if (flds.Count <= 0)
            return results;
        
        results = "[";
        for (int i = 0; i < flds.Count; ++i)
        {
            results += "[" + flds[i][0].ToString();
            for (int n = 1; n < flds[i].Count; ++n)
                results += ", " + flds[i][n].ToString();
            if (i < flds.Count - 1)
                results += "],";
            else
                results += "]";
        }

        return results + "]";
    }

    public void Main(string args)
    {
        string[] flds = args.Replace("[[","").Replace("]]","").Trim().Split("],[", StringSplitOptions.None);
        int[] nums = str_to_int_array(flds[0]);
        int target = int.Parse(flds[1]);
        Console.WriteLine("nums = " + output_int_array(nums));
        Console.WriteLine("target = " + target);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        List<List<int>> results = FourSum(nums, target);
        sw.Stop();

        Console.WriteLine("result = " + output_IList_array(results));
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
