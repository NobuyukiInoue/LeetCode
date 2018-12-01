using System;
using System.Collections.Generic;
using System.Linq;



public class Solution
{
    /*
    public class NumArray {

        int[] nums;
        public NumArray(int[] nums) {
            this.nums = nums;
        }
        
        public int SumRange(int i, int j) {
            int sum = 0;
            for (int n = i; n <= j && n < nums.Length; ++n)
                sum += nums[n];
            return sum;
        }
    }
    */
    public class NumArray
    {
        private int[] sum;

        public NumArray(int[] nums)
        {
            sum = new int[nums.Length + 1];
            for (int i = 0; i < nums.Length; i++) {
                sum[i + 1] = sum[i] + nums[i];
            }
        }

        public int SumRange(int i, int j)
        {
            return sum[j + 1] - sum[i];
        }    
    }

    private int[] set_array_int(string[] flds)
    {
        if (flds.Length == 0)
            return null;
        
        int[] nums = new int[flds.Length];
        for (int i = 0; i < flds.Length; ++i)
            nums[i] = int.Parse(flds[i]);

        return nums;
    }

    private string output_array_int(int[] nums)
    {
        if (nums.Length <= 0)
            return "";

        string resultStr = nums[0].ToString();
        for (int i = 1; i < nums.Length; ++i)
            resultStr += "," + nums[i].ToString();

        return resultStr;
    }

    public void Main(string args)
    {
        string[] flds = args.Replace("[","").Replace("]","").Split(',');
        int[] nums = set_array_int(flds);
        Console.WriteLine("nums = " + output_array_int(nums));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        NumArray obj = new NumArray(nums);
        Console.WriteLine("sumRange(0, 2) = " + obj.SumRange(0, 2));
        Console.WriteLine("sumRange(2, 5) = " + obj.SumRange(2, 5));
        Console.WriteLine("sumRange(0, 5) = " + obj.SumRange(0, 5));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
