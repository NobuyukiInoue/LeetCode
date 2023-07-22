using System;

public class Solution
{
    public void Merge(int[] nums1, int m, int[] nums2, int n)
    {
        // 149ms - 153ms
        int i = m - 1;
        int j = n - 1;
        int k = m + n - 1;
        while (j >= 0)
        {
            if (i >= 0 && nums1[i] > nums2[j])
            {
                nums1[k--] = nums1[i--];
            }
            else
            {
                nums1[k--] = nums2[j--];
            }
        }
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
        Console.WriteLine("args = " + args );
        String[] flds = args.Replace("[[[", "").Replace("]]]", "").Trim().Split("]],[[", StringSplitOptions.None);



        string[] str_args1 = flds[0].Split("],[", StringSplitOptions.None);
        int[] nums1 = str_to_int_array(str_args1[0]);
        int m = int.Parse(str_args1[1]);

        string[] str_args2 = flds[1].Split("],[", StringSplitOptions.None);
        int[] nums2 = str_to_int_array(str_args2[0]);
        int n = int.Parse(str_args2[1]);

        Console.WriteLine("nums1 = " + output_int_array(nums1) + ", m = " + m.ToString());
        Console.WriteLine("nums2 = " + output_int_array(nums2) + ", n = " + n.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        Merge(nums1, m, nums2, n);

        sw.Stop();
        Console.WriteLine("=== Results ===");
        Console.WriteLine("nums1 = " + output_int_array(nums1) + ", m = " + m.ToString());
        Console.WriteLine("nums2 = " + output_int_array(nums2) + ", n = " + n.ToString());
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
