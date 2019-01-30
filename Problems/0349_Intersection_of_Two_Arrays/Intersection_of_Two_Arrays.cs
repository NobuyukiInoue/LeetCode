using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {

    public int[] Intersection(int[] nums1, int[] nums2)
    {
	    return nums1.Intersect(nums2).Distinct().ToArray();
    }

    public int[] Intersection2(int[] nums1, int[] nums2)
    {
        HashSet <int>num1set=new HashSet <int>(nums1);
        HashSet <int>num2set=new HashSet <int>(nums2);
        List<int> res=new List<int>();
        foreach(int n in num2set)
            if(!num1set.Add(n)&&!res.Contains(n))
            res.Add(n);
        return res.ToArray();
    }

    public int[] Intersection_work(int[] nums1, int[] nums2)
    {
        List<int> result_nums = new List<int>();

        int i, j, k;
        bool hit;

        for (i = 0; i < nums2.Length; ++i) {
            for (j = 0; j < nums1.Length; ++j) {
                hit = false;
                for (k = 0; k < result_nums.Count; ++k) {
                    if (nums2[i] == result_nums[k]) {
                        hit = true;
                        break;
                    }
                }

                if (hit)
                    continue;
                
                if (nums2[i] == nums1[j])
                    result_nums.Add(nums2[i]);
            }
        }

        int[] nums = new int[result_nums.Count];
        for (i = 0; i < nums.Length; ++i)
            nums[i] = result_nums[i];

        return nums;
    }

    public int[] array_str_to_int(string[] workStr)
    {
        int[] nums = new int[workStr.Length];

        for (int i = 0; i < workStr.Length; ++i)
            nums[i] = int.Parse(workStr[i]);
        
        return nums;
    }

    public string output_array_int(int[] nums)
    {
        if (nums.Length == 0)
            return "";
        
        string resultStr = nums[0].ToString();
        for (int i = 1; i < nums.Length; ++i)
            resultStr += "," + nums[i].ToString();
        
        return resultStr;
    }

    public void Main(string args)
    {
        string temp = args.Replace("[[","").Replace("]]","");
        string[] flds = temp.Split(new string[] {"],["}, StringSplitOptions.None);
        string[] str_nums1 = flds[0].Split(',');
        string[] str_nums2 = flds[1].Split(',');
        int[] nums1 = array_str_to_int(str_nums1);
        int[] nums2 = array_str_to_int(str_nums2);
        Console.WriteLine("nums1 = " + output_array_int(nums1) + ", nums2 = " + output_array_int(nums2));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int[] result_nums = Intersection(nums1, nums2);
        Console.WriteLine("result_nums = " + output_array_int(result_nums));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
