using System;

// Definition for singly-linked list.

public class Solution {
    public int SingleNumber(int[] nums)
    {
        int i, j;
        bool[] nums_checked = new bool[nums.Length];

        for (i = 0; i < nums.Length; ++i) {
            
            if (nums_checked[i])
                continue;

            for (j = i + 1; j < nums.Length; ++j) {
                if (nums_checked[j])
                    continue;

                if (nums[i] == nums[j]) {
                    nums_checked[i] = nums_checked[j] = true;
                }
            }
            
            if (nums_checked[i] == false)
                return nums[i];
        }

        return -1;
    }

    public int SingleNumber_ver1(int[] nums)
    {
        int i, j;
        bool[] nums_checked = new bool[nums.Length];

        for (i = 0; i < nums.Length; ++i) {
            
            if (nums_checked[i])
                continue;

            for (j = i + 1; j < nums.Length; ++j) {
                if (nums_checked[j])
                    continue;

                if (nums[i] == nums[j]) {
                    nums_checked[i] = nums_checked[j] = true;
                }
            }
        }
        
        for (i = 0; i < nums.Length; ++i) {
            if (nums_checked[i] == false) {
                return nums[i];
            }
        }

        return -1;
    }

    private int[] array_str_to_int(string[] data)
    {
        int[] resultArray = new int[data.Length];

        for (int i = 0; i < data.Length; ++i)
        {
            resultArray[i] = int.Parse(data[i]);
        }
        
        return resultArray;
    }
    
    private string output_array_int(int[] nums)
    {
        string resultStr = nums[0].ToString();
        
        for (int i = 1; i < nums.Length; ++i)
        {
            resultStr += "," + nums[i].ToString();
        }
        
        return resultStr;
    }

    public void Main(string args)
    {
        string[] data = args.Split(',');
        int[] nums = array_str_to_int(data);
        Console.WriteLine("nums = " + output_array_int(nums));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        Console.WriteLine("Result = " + SingleNumber(nums));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
