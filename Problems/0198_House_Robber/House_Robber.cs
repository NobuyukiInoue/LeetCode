using System;
using System.Collections.Generic;

public class Solution {
    public int Rob(int[] nums)
    {
        if (nums.Length == 0)
            return 0;
        if (nums.Length == 1)
            return nums[0];

        int[] c = new int[nums.Length];
        int max;

        c[0] = nums[0];
        if (nums[0] >= nums[1])
            c[1] = nums[0];
        else
            c[1] = nums[1];

        max = c[1];
        
        for (int i = 2; i < nums.Length; ++i) {
            if (nums[i] + c[i - 2] >= c[i - 1])
                c[i] = nums[i] + c[i - 2];
            else
                c[i] = c[i - 1];
            
            if (max < c[i])
                max = c[i];
        }

        return max;
    }

    private int[] array_str_to_int(string[] workStr)
    {
        int[] numbers = new int[workStr.Length];

        for (int i = 0; i < workStr.Length; i++) {
            numbers[i] = int.Parse(workStr[i]);
        }

        return numbers;
    }

    private string output_array_int(int[] numbers)
    {
        if (numbers.Length == 0)
            return "";

        string resultStr = numbers[0].ToString();
        for (int i = 1; i < numbers.Length; i++)
            resultStr += "," + numbers[i].ToString();

        return resultStr;
    }

    public void Main(string args)
    {
        string[] numbersStr = args.Replace("[","").Replace("]","").Split(',');
        int[] nums = array_str_to_int(numbersStr);

        Console.WriteLine("numbers = [" + output_array_int(nums) + "]");

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();
        
        int result = Rob(nums);

        Console.WriteLine("result = " + result);
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
