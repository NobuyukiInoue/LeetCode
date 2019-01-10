using System;
using System.Linq;
using System.Collections.Generic;
//using System.Collections.ICollection;

public class Solution
{
    public IList<IList<int>> ThreeSum(int[] nums)
    {
        Array.Sort(nums);
        var result = new List<IList<int>>();
        for(var i = 0; i < nums.Length; i++)
        {
            if (i > 0 && nums[i] == nums[i - 1])
                continue;
            var j = i + 1;
            var k = nums.Length - 1;
            while(j < k)
            {
                if (j == i) 
                {
                    j++;
                    continue;
                }
                if (k == i)
                {
                    k--;
                    continue;
                }
                if (nums[i] + nums[j] + nums[k] < 0)
                {
                    j++;
                    continue;
                }
                if (nums[i] + nums[j] + nums[k] > 0)
                {
                    k--;
                    continue;
                }
                result.Add(new List<int> {nums[i], nums[j], nums[k]} );
                do
                {
                    j++;
                } while (j < k && nums[j] == nums[j - 1]);
                while (j < k && nums[k] == nums[k - 1])
                    k--;
            }
        }
        return result;
    }

    public IList<IList<int>> ThreeSum_work(int[] nums)
    {
        //IList<IList<int>> results = new IList<IList<int>>();
        var results = new List<List<int>>();

        for (int i = 0; i < nums.Length - 2; ++i)
        {
            for (int j = i + 1; j < nums.Length - 1; ++j)
            {
                for (int k = j + 1; k < nums.Length; ++k)
                {
                    if (nums[i] + nums[j] + nums[k] == 0)
                    {
                        //List<int> temp = new List<int> {nums[i], nums[j], nums[k]};
                        List<int> temp = new List<int>();
                        int[] temp_arr = new int[3] {nums[i], nums[j], nums[k]};
                        Array.Sort(temp_arr);
                        for (int t = 0; t < temp_arr.Length; ++t)
                            temp.Add(temp_arr[i]);
                        results.Add(temp);
                    }
                }
            }
        }
    
        return (IList<IList<int>>)results;
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

    public string output_IList_array(IList<IList<int>> flds)
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

        return "]" + results;
    }

    public void Main(string args)
    {
        string[] flds = args.Replace("[","").Replace("]","").Trim().Split(',');

        int[] nums = str_to_int_array(flds);
        Console.WriteLine("nums = " + output_int_array(nums));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        IList<IList<int>> results = ThreeSum(nums);
        Console.WriteLine("result = " + output_IList_array(results));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
