using System;
using System.Collections.Generic;

public class Solution
{
    public int[] Intersect(int[] nums1, int[] nums2)
    {
        if (nums1.Length <= 0 || nums2.Length <= 0)
            return new int[] {};
        
        List<int> resultList = new List<int>();
        Dictionary<int, int> dic = new Dictionary<int, int>();

        for (int i = 0; i < nums1.Length; ++i)
        {
            if (!dic.ContainsKey(nums1[i]))
                dic.Add(nums1[i], 1);
            else
                dic[nums1[i]]++;
        }

        for (int j = 0; j < nums2.Length; ++j)
        {
            if (dic.ContainsKey(nums2[j]))
            {
                resultList.Add(nums2[j]);
                dic[nums2[j]]--;
                if ((int)dic[nums2[j]] == 0)
                    dic.Remove(nums2[j]);
            }
        }

        return resultList.ToArray();
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
        string[] nums_str = args.Trim().Replace("[[", "").Replace("]]", "").Split(new string[] {"],["}, StringSplitOptions.None);
        int[] nums1 = str_to_int_array(nums_str[0]);
        int[] nums2 = str_to_int_array(nums_str[1]);
        Console.WriteLine("nums1 = " + output_int_array(nums1));
        Console.WriteLine("nums2 = " + output_int_array(nums2));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int[] result = Intersect(nums1, nums2);
        Console.WriteLine("result = " + output_int_array(result));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
