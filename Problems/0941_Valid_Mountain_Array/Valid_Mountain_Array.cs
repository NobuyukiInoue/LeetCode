using System;
using System.Linq;

public class Solution
{
    public bool ValidMountainArray(int[] A)
    {
        if (A.Length < 3 || A[0] > A[1])
            return false;

        bool peak_passed = false;
        for (int i = 1; i < A.Length; ++i)
        {
            if (A[i-1] == A[i])
                return false;
            else if (!peak_passed && A[i-1] > A[i])
                peak_passed = true;
            else if (peak_passed && A[i-1] < A[i])
                return false;
        }
        return peak_passed;        
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

        int[] A = str_to_int_array(flds);
        Console.WriteLine("A = " + output_int_array(A));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        bool results = ValidMountainArray(A);
        Console.WriteLine("result = " + results.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
