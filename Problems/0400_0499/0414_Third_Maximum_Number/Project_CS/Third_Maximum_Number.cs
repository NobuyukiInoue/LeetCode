using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public int ThirdMax(int[] nums)
    {
        int m = 0, m2 = 0, m3 = 0, c = 0;

        foreach(var n in nums) {
            if(c == 0 || n > m) {
                m3 = m2;
                m2 = m;
                m = n;
            } else if(n < m && (c == 1 || n > m2)) {
                m3 = m2;
                m2 = n;
            } else if(n < m2 && (c == 2 || n > m3)) {
                m3 = n;
            } else {
                continue;
            }
            c++;
        }
        
        return c > 2 ? m3 : m;
    }

    public int ThirdMax2(int[] nums)
    {
        int[] array_max = new int[3] { 0, 0, 0 };
        int count = 0;

        for (int i = 0; i < nums.Length; ++i) {
            if (nums[i] > array_max[0] || count == 0) {
                array_max[2] = array_max[1];
                array_max[1] = array_max[0];
                array_max[0] = nums[i];
            }
            else if ((nums[i] > array_max[1] || count == 1) && nums[i] < array_max[1]) {
                array_max[2] = array_max[1];
                array_max[1] = nums[i];
            }
            else if ((nums[i] > array_max[2] || count == 2) && nums[i] < array_max[2]) {
                array_max[2] = nums[i];
            }
            else {
                continue;
            }

            count++;
        }

        if (count > 2)
            return array_max[2];
        else
            return array_max[0];
    }

    private void output_maxs(int[] array_max, int count)
    {
        Console.WriteLine("max[0] = " + array_max[0] + ", max[1] = " + array_max[1] + ", max[2] = " + array_max[2] + ", count = " + count);
    }

    private int[] set_array_int(string[] flds)
    {
        if (flds.Length == 0)
            return null;
        
        int[] nums = new int[flds.Length];
        for (int i = 0; i < flds.Length; ++i)
            nums[i] = int.Parse(flds[i]);

        return nums;
    }

    private string output_array_int(int[] nums)
    {
        if (nums.Length <= 0)
            return "";

        string resultStr = nums[0].ToString();
        for (int i = 1; i < nums.Length; ++i)
            resultStr += "," + nums[i].ToString();

        return resultStr;
    }

    public void Main(string args)
    {
        string[] flds = args.Replace("[","").Replace("]","").Split(',');
        int[] nums = set_array_int(flds);
        Console.WriteLine("nums = " + output_array_int(nums));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = ThirdMax(nums);
        Console.WriteLine("nums = " + result);
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
