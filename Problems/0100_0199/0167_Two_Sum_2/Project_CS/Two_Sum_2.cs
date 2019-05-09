using System;
using System.Collections.Generic;

public class Solution {
    public int[] TwoSum1(int[] numbers, int target)
    {
        int l = 0, r = numbers.Length - 1;
        int s;
        while (l < r) {
            s = numbers[l] + numbers[r];
            if (s == target)
                return (new int[] {l + 1, r + 1});
            else if (s < target)
                ++l;
            else
                --r;
        }

        return (new int[] {0,0});
    }

    public int[] TwoSum3(int[] numbers, int target)
    {
        for (int i = 0; i < numbers.Length; ++i) {
            int l = i + 1;
            int r = numbers.Length - 1;
            int tmp = target - numbers[i];
            int mid;
            while (l <= r) {
                mid = l + (r - l)/2;
                if (numbers[mid] == tmp)
                    return (new int[] {i+1, mid + 1});
                else if (numbers[mid] < tmp)
                    l = mid + 1;
                else
                    r = mid - 1;
            }
        }

        return (new int[] {0,0});
    }

    public int[] TwoSum_work(int[] numbers, int target)
    {
        int[] resultNumbers = new int [2];
        int i, j;

        for (i = 0; i < numbers.Length; ++i) {
            if (i > 1 && numbers[i] == numbers[i - 1])
                continue;

            resultNumbers[0] = i + 1;

            for (j = i + 1; j < numbers.Length; ++j) {
                if (numbers[i] + numbers[j] == target) {
                    resultNumbers[1] = j + 1;
                    return resultNumbers;
                }
                else {
                    if (numbers[j] == numbers[j - 1])
                        break;
                    if (numbers[i] + numbers[j] > target)
                        break;
                    if (target > 0 && numbers[j] > target)
                        break;
                }
            }
        }

        return resultNumbers;
    }

    public int[] str_to_int_array(string s)
    {
        if (s.Length <= 0)
            return null;

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
        int[] numbers = str_to_int_array(flds[0]);
        int target = int.Parse(flds[1]);

        Console.WriteLine("numbers = " + output_int_array(numbers));
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

    //  int[] result = TwoSum_work(numbers, target);
        int[] result = TwoSum1(numbers, target);
    //  int[] result = TwoSum3(numbers, target);

        Console.WriteLine("Result = " + output_int_array(result));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
