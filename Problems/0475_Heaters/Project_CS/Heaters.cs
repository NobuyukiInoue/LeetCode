using System;
using System.Linq;

public class Solution
{
    public int FindRadius(int[] houses, int[] heaters)
    {
            houses = houses.OrderBy(x => x).ToArray();
            heaters = heaters.OrderBy(x => x).ToArray();

            int ret = 0;
            for (int i = 0, j = 0; i < heaters.Length && j < houses.Length;)
            {
                if (houses[j] <= heaters[i] && i == 0)
                {
                    ret = Math.Max(ret, heaters[i] - houses[j]);
                    j++;
                }
                else if (houses[j] >= heaters[i] && i == heaters.Length - 1)
                {
                    ret = Math.Max(ret, houses[j] - heaters[i]);
                    j++;
                }
                else if (i!= heaters.Length - 1 && houses[j] >= heaters[i] && houses[j] <= heaters[i + 1])
                {
                    ret = Math.Max(ret, Math.Min(houses[j] - heaters[i], heaters[i + 1] - houses[j]));
                    j++;
                }
                else
                {
                    i++;
                }
            }

            return ret;
        
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

    public string output_int_array(int[] nums)
    {
        if (nums.Length <= 0)
            return "";

        string resultStr = "[" +  nums[0].ToString();
 
        for (int i = 1; i < nums.Length / 2; ++i)
        {
            resultStr += "," + nums[i].ToString();
        }

        return resultStr + "]";
    }

    public void Main(string args)
    {
        string temp = args.Replace("[[","").Replace("]]","").Trim();
        string[] flds = temp.Split(new string[] {"],["}, StringSplitOptions.None);
        int[] houses = str_to_int_array(flds[0]);
        int[] heaters = str_to_int_array(flds[1]);

        Console.WriteLine("houses = " + output_int_array(houses));
        Console.WriteLine("heaters = " + output_int_array(heaters));
        
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = FindRadius(houses, heaters);
        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
