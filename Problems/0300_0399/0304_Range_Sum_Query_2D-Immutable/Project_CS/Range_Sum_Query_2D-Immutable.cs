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

    private void NumMatrix_Main(string[] ope, string[] para)
    {
        if (ope.Length != para.Length)
            return;
        if (ope.Length <= 0 || para.Length <= 0)
            return;

        string[] matrix_str = para[0].Replace("[[", "").Replace("]]", "").Split("],[",  StringSplitOptions.None);
        int[][] matrix = new int[matrix_str.Length][];
        for (int n = 0; n < matrix.Length; n++) {
            matrix[n] = set_array_int(matrix_str[n].Split(','));
        }

        NumMatrix nm = new NumMatrix(matrix);

        for (int i = 0; i < ope.Length; i++)
        {
            if (ope[i] == "NumMatrix")
            {
                Console.WriteLine("NumMatrix()");
            }
            else if (ope[i] == "sumRegion")
            {
                string[] flds = para[i].Split(',');
                int row1 = int.Parse(flds[0]);
                int col1 = int.Parse(flds[1]);
                int row2 = int.Parse(flds[2]);
                int col2 = int.Parse(flds[3]);
                int sum = nm.SumRegion(row1, col1, row2, col2);
                Console.WriteLine("sumRegion(" + row1.ToString()
                                  + ", " + col1.ToString()
                                  + ", " + row2.ToString()
                                  + ", " + col2.ToString()
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
        string[] flds = args.Replace("\"", "").Trim().Split("],[[[[", StringSplitOptions.None);
        string[] ope = flds[0].Replace("\"", "").Replace("[", "").Replace("]", "").Split(',');
        string[] para;
        if (flds.Length > 1) {
            string[] params_str1 = flds[1].Split("]]],[", StringSplitOptions.None);
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

        NumMatrix_Main(ope, para);

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
