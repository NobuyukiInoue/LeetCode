using System;
using System.Linq;
public class Solution
{
    public int ArrayPairSum(int[] nums)
    {
        Array.Sort(nums);
        int sum = 0;
        for (int i = 0; i < nums.Length; i += 2)
            sum += nums[i];
        
        return sum;
    }

    public int[] str_to_int_array(string nums_str)
    {
        string[] flds = nums_str.Split(",");

        int[] nums = new int[flds.Length];
        for (int i = 0; i < nums.Length; ++i)
            nums[i] = int.Parse(flds[i]);

        return nums;
    }
    public string output_str_array(string[] words)
    {
        if (words.Length <= 0)
            return "";
        
        string results = words[0];
        for (int i = 1; i < words.Length; ++i)
        {
            results += ", " + words[i];
        }

        return results;
    }

    public void Main(string args)
    {
        string nums_str = args.Replace("\"","").Replace(" ","").Replace("[","").Replace("]","").Trim();
        int[] nums = str_to_int_array(nums_str);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = ArrayPairSum(nums);
        
        sw.Stop();

        Console.WriteLine("result = " + result.ToString());
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
