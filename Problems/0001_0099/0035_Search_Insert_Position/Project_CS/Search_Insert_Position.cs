using System;

public class Solution {
    public int SearchInsert(int[] nums, int target)
    {
        int i;
        
        for ( i = 0; i < nums.Length; i++ ) {
            if ( nums[i] < target ) {
                continue;
            }
            else if ( nums[i] >= target ) {
                return i;
            }
        }
        
        return i;
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
        string arg_str = args.Replace("[[","").Replace("]]","").Trim();
        string[] flds = arg_str.Split(new string[] {"],["}, StringSplitOptions.None);
        int[] nums = str_to_int_array(flds[0]);
        int target = int.Parse(flds[1]);

        Console.WriteLine("nums = " + output_int_array(nums));
        Console.WriteLine("target = " + target.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = SearchInsert(nums, target);
        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
