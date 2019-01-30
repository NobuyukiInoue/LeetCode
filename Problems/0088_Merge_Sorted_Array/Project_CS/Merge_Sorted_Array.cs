using System;

public class Solution
{
    public void Merge(int[] nums1, int m, int[] nums2, int n)
    {
        /*
        if (nums1.Length < nums2.Length)
        {
            Console.WriteLine("n not equal nums2.Length!!!");
            return;
        }
        if (nums2.Length != n) {
            Console.WriteLine("n not equal nums2.Length!!!");
            return;
        }
        */
        int index_num1 = m - 1;
        int i = nums1.Length - 1;
        int j = nums2.Length - 1;

        while (i >= 0 && j >= 0) {
            if (index_num1 >= 0) {
                if ((nums1[index_num1] > nums2[j])) {
                    nums1[i--] = nums1[index_num1--];
                }
                else {
                    nums1[i--] = nums2[j--];
                }
            }
            else {
                nums1[i--] = nums2[j--];
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
