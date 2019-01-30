using System;

public class Solution
{
    public bool CanPlaceFlowers(int[] flowerbed, int n)
    {
        if (flowerbed.Length == 0)
            return false;
        if (n == 0)
            return true;
        
        int plant = 0;
        for (int i = 0; i < flowerbed.Length; ++i)
        {
            if (flowerbed[i] == 1)
                continue;
            if (i != 0)
                if (flowerbed[i - 1] == 1)
                    continue;
            if (i != flowerbed.Length - 1) 
                if (flowerbed[i + 1] == 1)
                    continue;
            plant += 1;
            flowerbed[i] = 1;
        }

        return (n <= plant);
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
        string arg_str = args.Replace("[[","").Replace("]]","").Trim();
        string[] flds = arg_str.Split(new string[] {"],["}, StringSplitOptions.None);
        int[] flowerbed = str_to_int_array(flds[0]);
        int n = int.Parse(flds[1]);

        Console.WriteLine("nums = " + output_int_array(flowerbed));
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        bool result = CanPlaceFlowers(flowerbed, n);
        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
