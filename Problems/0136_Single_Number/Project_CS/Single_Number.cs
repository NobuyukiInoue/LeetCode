using System;

public class Solution
{
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
        string flds = args.Replace("\"", "").Replace(" ", "").Replace("[", "").Replace("]", "");
        int[] nums = str_to_int_array(flds);
        Console.WriteLine("prices[] = " + output_int_array(nums));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = SingleNumber(nums);

        sw.Stop();
        Console.WriteLine("Result = " + result.ToString());
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
