using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public int[] SortedSquares(int[] A)
    {
        int[] squareA = new int[A.Length];
        for (int i = 0; i < A.Length; ++i)
        {
            squareA[i] = A[i] * A[i];
        }

        Array.Sort(squareA);
        return squareA;
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

        int[] result = SortedSquares(A);
        Console.WriteLine("result = " + output_int_array(result));

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
