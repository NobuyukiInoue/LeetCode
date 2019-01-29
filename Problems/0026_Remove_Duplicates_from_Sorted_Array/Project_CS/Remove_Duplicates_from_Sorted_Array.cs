using System;

public class Solution {
    public int RemoveDuplicates(int[] nums)
    {
        if (nums.Length == 0)
            return 0;

        int i = 1, n = 1;
        for ( ; i < nums.Length; i++ ) {
               if (nums[i] > nums[i - 1]) {
                   nums[n++] = nums[i];
            }
        }
        
        return n;
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
        int[] nums = str_to_int_array(flds);
        Console.WriteLine("num = " + output_int_array(nums));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = RemoveDuplicates(nums);
        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
