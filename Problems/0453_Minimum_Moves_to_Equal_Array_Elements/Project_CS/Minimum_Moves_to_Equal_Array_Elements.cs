using System;

public class Solution
{
    /*
    public int MinMoves_submission(int[] nums)
    {
        long sum = 0;

        foreach (var num in nums)
            sum += num;

        sum -= nums.Min() * nums.Length;

        return (int) sum;
    }
    */
    public int MinMoves(int[] nums)
    {
        return sum(nums) - min(nums) * nums.Length;
    }

    public int sum(int[] nums)
    {
        int sum = 0;
        for (int i = 0; i < nums.Length; ++i)
        {
            sum += nums[i];
        }

        return sum;
    }

    public int min(int[] nums)
    {
        int min = int.MaxValue;
        for (int i = 0; i < nums.Length; ++i)
        {
            if (nums[i] < min)
                min = nums[i];
        }

        return min;
    }
    public int[] str_to_int_array(string[] flds)
    {
        if (flds.Length <= 0)
            return null;

        int[] nums = new int[flds.Length];

        for (int i = 0; i < flds.Length; ++i)
        {
            nums[i] = int.Parse(flds[i]);
        }

        return nums;
    }

    public string output_points(int[] nums)
    {
        if (nums.Length <= 0)
            return "";

        string resultStr = "[" + nums[0].ToString();

        for (int i = 1; i < nums.Length; ++i)
        {
            resultStr += "," + nums[i].ToString();
        }

        return resultStr + "]";
    }

    public void Main(string args)
    {
        string temp = args.Replace("[","").Replace("]","").Trim();
        string[] flds = temp.Split(',');
        int[] nums = str_to_int_array(flds);

        Console.WriteLine("nums = " + output_points(nums));
        
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = MinMoves(nums);
        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
