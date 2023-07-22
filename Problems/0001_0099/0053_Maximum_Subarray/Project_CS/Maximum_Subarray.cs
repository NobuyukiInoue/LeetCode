using System;

public class Solution
{
    public int MaxSubArray(int[] nums)
    {
        // 212ms
        int maxSum = int.MinValue, currentSum = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            currentSum += nums[i];
            if (currentSum > maxSum)
                maxSum = currentSum;
            if (currentSum < 0)
                currentSum = 0;
        }
        return maxSum;
    }

    private void output(int[] nums, int pos1, int pos2, int maxSum)
    {
        for (int i = 0; i < nums.Length; i++ )
            if ( i < nums.Length - 1)
                Console.Write(nums[i].ToString() + ",");
            else
                Console.WriteLine(nums[i].ToString());

        Console.WriteLine("pos1 = " + pos1.ToString() + ", pos2 = " + pos2.ToString());
        Console.WriteLine("maxSum = " + maxSum.ToString() );

        for (int i = pos1; i <= pos2; i++ )
            if ( i < pos2 )
                Console.Write(nums[i].ToString() + ",");
            else
                Console.WriteLine(nums[i].ToString());
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
        string flds = args.Replace(" ","").Replace("[","").Replace("]","").Trim();
        int[] nums = str_to_int_array(flds);

        Console.WriteLine("nums = " + output_int_array(nums));
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = MaxSubArray(nums);
        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
