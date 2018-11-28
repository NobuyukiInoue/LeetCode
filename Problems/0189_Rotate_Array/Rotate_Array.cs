using System;
using System.Collections.Generic;

public class Solution {
    public void Rotate(int[] nums, int k) {
        int[] temp_nums = new int[nums.Length];
        Array.Copy(nums, temp_nums, nums.Length);
        
        for (int i = 0; i < nums.Length; ++i) {
            if (i + k < nums.Length)
                nums[i + k] = temp_nums[i];
            else
                nums[(i + k) % nums.Length] = temp_nums[i];
        }
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
        string[] flds = args.Split(new string[] {", "}, StringSplitOptions.None);
        string[] numbersStr = flds[0].Replace("[","").Replace("]","").Split(',');
        int[] numbers = array_str_to_int(numbersStr);
        int target = int.Parse(flds[1]);

        Console.WriteLine("numbers = [" + output_array_int(numbers) + "], target = " + target);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();
        
        Rotate(numbers, target);

        Console.WriteLine("nums(result) = " + output_array_int(numbers));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
