using System;
using System.Linq;

public class Solution
{
    public int MaxArea(int[] height)
    {
        int leftHigh = 0;
        int rightHigh = height.Length - 1;
        int maxArea = 0;

        while (leftHigh < rightHigh)
        {
            if (height[leftHigh] < height[rightHigh])
            {
                int curArea = height[leftHigh] *(rightHigh - leftHigh);
                if (curArea > maxArea)
                {
                    maxArea = curArea;
                }
                leftHigh++;
            }
            else
            {
                int curArea = height[rightHigh] *(rightHigh - leftHigh);
                if (curArea > maxArea)
                {
                    maxArea = curArea;
                }
                rightHigh--;
            }
        }

        return maxArea;
    }

    public int[] str_to_int_array(string[] flds)
    {
        if (flds.Length <= 0)
            return null;

        int[] nums = new int[flds.Length];
        for (int i = 0; i < nums.Length; ++i)
        {
            nums[i] = int.Parse(flds[i]);
        }

        return nums;
    }

    public string output_int_array(int[] flds)
    {
        string results = "";
        if (flds.Length <= 0)
            return results;
        
        results = flds[0].ToString();
        for (int i = 1; i < flds.Length; ++i)
        {
            results += ", " + flds[i].ToString();
        }

        return results;
    }

    public string output_str_array(string[] flds)
    {
        string results = "";
        if (flds.Length <= 0)
            return results;
        
        results = flds[0];
        for (int i = 1; i < flds.Length; ++i)
        {
            results += ", " + flds[i];
        }

        return results;
    }

    public void Main(string args)
    {
        string[] flds = args.Replace("[","").Replace("]","").Trim().Split(',');

        int[] height = str_to_int_array(flds);
        Console.WriteLine("height = " + output_int_array(height));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int results = MaxArea(height);
        Console.WriteLine("result = " + results.ToString());

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
