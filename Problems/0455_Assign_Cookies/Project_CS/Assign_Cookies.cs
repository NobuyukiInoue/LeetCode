using System;

public class Solution
{
    public int FindContentChildren(int[] g, int[] s)
    {
        Array.Sort(g);
        Array.Sort(s);

        int g_length = g.Length - 1;
        int gave_cookies = 0;

        foreach (int select_cookies in s)
            if (gave_cookies > g_length)
                break;
            else if (g[gave_cookies] <= select_cookies)
                gave_cookies++;

        return gave_cookies;
    }

    public int[] str_to_int_array(string flds)
    {
        if (flds.Length <= 0)
            return null;
        
        string[] temp = flds.Split(',');
        int[] nums = new int[temp.Length];
        for (int i = 0; i < temp.Length; ++i)
        {
            nums[i] = int.Parse(temp[i]);
        }

        return nums;
    }

    public string output_array(int[] nums)
    {
        if (nums.Length <= 0)
            return "";
        
        string resultStr = "[" + nums[0].ToString();
        for (int i = 1; i < nums.Length; ++i)
        {
            resultStr += "," + nums[i].ToString();
        }
        resultStr += "]";

        return resultStr;
    }

    public void Main(string args)
    {
        string temp = args.Replace("[[","").Replace("]]","").Trim();
        string[] flds = temp.Split(new string[] {"],["}, StringSplitOptions.None);
        int[] g = str_to_int_array(flds[0]);
        int[] s = str_to_int_array(flds[1]);

        Console.WriteLine("g[] = " + output_array(g));
        Console.WriteLine("s[] = " + output_array(s));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = FindContentChildren(g, s);
        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
