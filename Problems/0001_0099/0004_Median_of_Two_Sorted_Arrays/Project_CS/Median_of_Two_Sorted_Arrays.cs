using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public double FindMedianSortedArrays(int[] nums1, int[] nums2)
    {
        int cnt = 0, i = 0, j = 0;
        List<double> MergeList = new List<double>();
        int medianindex = Medianindex(nums1, nums2, out bool even);

        if (even == false) 
        {
            medianindex = medianindex + 1;
        }

        while (cnt < medianindex )
        {
            if(nums2.Length == j || (nums1.Length > i && nums1[i]<= nums2[j]))
            {
                cnt++;
                MergeList.Add(nums1[i]);
                i++;
            }
            else if (nums1.Length == i || (nums2.Length > j && nums1[i] > nums2[j]))
            {
                cnt++;
                MergeList.Add(nums2[j]);
                j++;
            }
        }

        return even == true ? (MergeList[MergeList.Count - 1] + MergeList[MergeList.Count - 2] ) /2  : MergeList[MergeList.Count - 1];
    }

    public int Medianindex(int[] nums1, int[] nums2, out bool even)
    {
        int TotalLength = nums1.Length + nums2.Length;
        
        even = true;
        if (TotalLength % 2 == 1)
        {
            even = false;
        }

        int medianIndex = TotalLength / 2;
        return even == true ? medianIndex +1 : medianIndex ;
    }

    public double FindMedianSortedArrays2(int[] nums1, int[] nums2)
    {
        int[] all_nums = nums1.Concat(nums2).ToArray();
        Array.Sort(all_nums);
        
        if (all_nums.Length % 2 == 1){
            return(all_nums[all_nums.Length / 2]);
        }
        else
        {
            return((double)(all_nums[all_nums.Length/2 - 1] + all_nums[all_nums.Length/2])/ 2);
        }
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
        string[] flds = args.Replace("\"","").Replace("[[","").Replace("]]","").Trim().Split("],[", StringSplitOptions.None);
        int[] nums1 = str_to_int_array(flds[0]);
        int[] nums2 = str_to_int_array(flds[1]);

        Console.WriteLine("nums1 = " + output_int_array(nums1));
        Console.WriteLine("nums2 = " + output_int_array(nums2));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        double result = FindMedianSortedArrays(nums1, nums2);
        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
