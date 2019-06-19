using System;
using System.Collections.Generic;

public class Solution
{
    private string stringArray2string(string[] words)
    {
        if (words.Length <= 0)
            return "";
        
        string resultStr = "[[" + words[0];
        for (int i = 1; i < words.Length; i++)
        {
            resultStr += "],[" + words[i];
        }

        return resultStr + "]]";
    }

    private void NumArray_Main(string[] ope, string[] para)
    {
        if (ope.Length != para.Length)
            return;
        if (ope.Length <= 0 || para.Length <= 0)
            return;

        int[] nums = set_array_int(para[0].Split(','));

        NumArray nm = new NumArray(nums);

        for (int n = 0; n < ope.Length; n++)
        {
            if (ope[n] == "NumArray")
            {
                Console.WriteLine("NumArray()");
            }
            else if (ope[n] == "update")
            {
                string[] flds = para[n].Split(',');
                int i = int.Parse(flds[0]);
                int val = int.Parse(flds[1]);
                nm.Update(i, val);
                Console.WriteLine("update(" + i.ToString()
                                  + ", " + val.ToString()
                                  + ")");
            }
            else if (ope[n] == "sumRange")
            {
                string[] flds = para[n].Split(',');
                int i = int.Parse(flds[0]);
                int j = int.Parse(flds[1]);
                int sum = nm.SumRange(i, j);
                Console.WriteLine("sumRange(" + i.ToString()
                                  + ", " + j.ToString()
                                  + ") = " + sum.ToString());
            }
        }
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

    public void Main(string args)
    {
        string[] flds = args.Replace("\"", "").Trim().Split("],[[[", StringSplitOptions.None);
        string[] ope = flds[0].Replace("\"", "").Replace("[", "").Replace("]", "").Split(',');
        string[] para;
        if (flds.Length > 1) {
            string[] params_str1 = flds[1].Split("]],[", StringSplitOptions.None);
            string[] params_str2 = params_str1[1].Replace("]]]", "").Split("],[", StringSplitOptions.None);

            para = new string[1 + params_str2.Length];
            para[0] = params_str1[0];
            for (int i = 0; i < params_str2.Length; i++) {
                para[i + 1] = params_str2[i].Replace("[", "").Replace("]", "");
            }
        }
        else {
            para = new string[0];
        }
        Console.WriteLine("ope[] = " + stringArray2string(ope));
        Console.WriteLine("para[] = " + stringArray2string(para));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        NumArray_Main(ope, para);

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
