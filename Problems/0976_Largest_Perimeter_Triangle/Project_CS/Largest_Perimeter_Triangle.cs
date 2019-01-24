using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public int LargestPerimeter(int[] A)
    {
        Array.Sort(A);
        for (int i = A.Length - 1; i > 1; --i)
            if (A[i] < A[i - 1] + A[i - 2])
                return A[i] + A[i - 1] + A[i - 2];
        return 0;
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
        string flds = args.Replace("[","").Replace("]","").Trim();
        int[] A = str_to_int_array(flds);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = LargestPerimeter(A);
        Console.WriteLine("result = " + result.ToString());

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
