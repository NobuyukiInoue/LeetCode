using System;

public class Solution
{
    public int MaxSubArray(int[] nums)
    {
        int i, j;
        int sum;
    //  int pos1 = 0, pos2 = 0;
        int max_sum = nums[0];
        
        for ( i = 0; i < nums.Length; ++i ) {
            if ( nums[i] < 0 && max_sum > 0) {
                continue;
            }

            sum = nums[i];

            if (sum > max_sum) {
                max_sum = sum;
            //  pos1 = pos2 = i;
            }

            for ( j = i + 1; j < nums.Length; ++j ) {
                sum += nums[j];

                if (sum > max_sum) {
                    max_sum = sum;
                //  pos1 = i;
                //  pos2 = j;
                }
            }
        }

    //  output(nums, pos1, pos2, max_sum);

        return max_sum;
    }

    private void output(int[] nums, int pos1, int pos2, int max_sum)
    {
        for (int i = 0; i < nums.Length; i++ )
            if ( i < nums.Length - 1)
                Console.Write(nums[i].ToString() + ",");
            else
                Console.WriteLine(nums[i].ToString());

        Console.WriteLine("pos1 = " + pos1.ToString() + ", pos2 = " + pos2.ToString());
        Console.WriteLine("max_sum = " + max_sum.ToString() );

        for (int i = pos1; i <= pos2; i++ )
            if ( i < pos2 )
                Console.Write(nums[i].ToString() + ",");
            else
                Console.WriteLine(nums[i].ToString());
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
        string flds = args.Replace(" ","").Replace("[","").Replace("]","").Trim();
        int[] nums = str_to_int_array(flds);

        Console.WriteLine("nums = " + output_int_array(nums));
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = MaxSubArray(nums);
        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
