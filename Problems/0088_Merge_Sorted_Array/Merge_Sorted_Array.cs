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

    private int[] array_str_to_int(string[] workStr)
    {
        int[] nums = new int[workStr.Length];

        for (int i = 0; i < workStr.Length; i++) {
            nums[i] = int.Parse(workStr[i]);
        }

        return nums;
    }

    private void output_array(int[] data, string name, int mn)
    {
        Console.Write("int[" + data.Length.ToString() + "] = ");

        for (int i = 0; i < data.Length - 1; ++i) {
            Console.Write(data[i].ToString() + ",");
        }
        Console.Write(data[data.Length - 1].ToString());
        Console.WriteLine("  " + name + mn.ToString());
    }

    public void Main(string args)
    {
        Console.WriteLine("args = " + args );

    //    string[] workStr = args.Split('\t');
        string[] workStr = args.Split((char)0x09);    // [TAB]

        string[] arg1 = workStr[0].Split(':');
        string[] arg2 = workStr[1].Split(':');

        string[] arg1_array = arg1[0].Split(',');
        int[] nums1 = array_str_to_int(arg1_array);
        int m = int.Parse(arg1[1]);

        string[] arg2_array = arg2[0].Split(',');
        int[] nums2 = array_str_to_int(arg2_array);
        int n = int.Parse(arg2[1]);

        output_array(nums1, "m = ", m);
        output_array(nums2, "n = ", n);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        Merge(nums1, m, nums2, n);

        Console.WriteLine("=== Results ===");
        output_array(nums1, "m = ", m);
        output_array(nums2, "n = ", n);

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
