using System;

public class Solution
{
    public int[,] MatrixReshape(int[,] nums, int r, int c) {
        var r2 = nums.GetLength(0);
        var c2 = nums.GetLength(1);

        if (r2 *c2 != r * c)
            return nums;

        int[,] result = new int[r, c];

        for (var i = 0; i < r2; i++){
            for (var j = 0; j < c2; j++){
                var position = (i*c2) + j;
                result[position / c, position % c] = nums[i,j];
            }
        }
        return result;
    }

    public int[,] MatrixReshape_work(int[,] nums, int r, int c) 
    {
        if (c*r != nums.Length)
            return nums;

        int[,] resultArray = new int[r, c];
        int row = 0, col = 0;

        for (int i = 0; i < nums.GetLength(0); ++i)
        {
            for (int j = 0; j < nums.GetLength(1); ++j)
            {
                resultArray[row, col++] = nums[i, j];
                if (col >= c)
                {
                    col = 0;
                    row++;
                }
            }
        }

        return resultArray;
    }

    public int[] str_to_int_array(string s)
    {
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

    public string output_int_2D_array(int[,] nums)
    {
        if (nums.Length <= 0)
            return "";

        string resultStr = "[";
        for (int i = 0; i < nums.GetLength(0); ++i)
        {
            if (i == 0)
                resultStr += "[";
            else
                resultStr += ",[";

            for (int j = 0; j < nums.GetLength(1); ++j)
                if (j == 0)
                    resultStr += nums[i, j].ToString();
                else
                    resultStr += "," + nums[i, j].ToString();
            resultStr += "]";
        }

        return resultStr + "]";
    }

    public void Main(string args)
    {
        string[] args_str = args.Trim().Split(new string[] {"]],"}, StringSplitOptions.None);
        string[] nums_str = args_str[0].Replace("[[", "").Split(new string[] {"],["}, StringSplitOptions.None);

        string[] second_fld = nums_str[0].Split(',');
        int[,] nums = new int[nums_str.Length, second_fld.Length];

    //  Console.WriteLine("nums_str.Length = " + nums_str.Length.ToString());
        for (int i = 0; i < nums.GetLength(0); ++i)
        {
        //  Console.WriteLine("nums_str = " + nums_str[i]);
            second_fld = nums_str[i].Split(',');
            for (int j = 0; j < nums.GetLength(1); ++j)
            {
                try
                {
                    nums[i, j] = int.Parse(second_fld[j]);
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                    Console.WriteLine("second_fld.Length = " + second_fld.Length);
                    Environment.Exit(-1);
                }
            }
        }

        string[] r_and_c = args_str[1].Split(',');
        int r = int.Parse(r_and_c[0]);
        int c = int.Parse(r_and_c[1]);

        Console.WriteLine("nums = " + output_int_2D_array(nums));
        Console.WriteLine("r = " + r.ToString() + ", c = " + c.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int[,] result = MatrixReshape(nums, r, c);
        Console.WriteLine("result = " + output_int_2D_array(result));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
