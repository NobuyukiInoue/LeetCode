using System;
using System.Linq;

public class Solution
{
    public string LargestTimeFromDigits(int[] A)
    {
        Array.Sort(A);
        Array.Reverse(A);
        int su = 0, sd = 0;
        for (int i1 = 0; i1 < A.Length; ++i1)
        {
            for (int i2 = 0; i2 < A.Length; i2++)
            {
                if (i2 == i1)
                    continue;
                for (int i3 = 0; i3 < A.Length; ++i3)
                {
                    if (i3 == i1 || i3 == i2)
                        continue;
                    for (int i4 = 0; i4 < A.Length; ++i4)
                    {
                        if (i4 == i1 || i4 == i2 || i4 == i3)
                            continue;
                        su = (A[i1]*10 + A[i2]);
                        sd = (A[i3]*10 + A[i4]);
                        if (su < 24 && sd < 60)
                            return A[i1].ToString() + A[i2].ToString() + ":" + A[i3].ToString() + A[i4].ToString();
                    }
                }
            }
        }
        return "";
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

    public void Main(string args)
    {
        string[] flds = args.Replace("[","").Replace("]","").Trim().Split(',');

        int[] A = str_to_int_array(flds);
        Console.WriteLine("A = " + output_int_array(A));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        string results = LargestTimeFromDigits(A);
        Console.WriteLine("result = " + results);
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
