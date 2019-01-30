using System;
using System.Text;

public class Solution
{
    public int[] PlusOne(int[] digits)
    {
        int retVal_Length;

        if (Check_Carry(digits)) {
            retVal_Length = digits.Length + 1;
        }
        else {
            retVal_Length = digits.Length;
        }

        int[] retVal = new int[retVal_Length];

//        output_IntVal( digits );
//        output_IntVal( retVal );

        retVal[retVal_Length - 1] = 1;

//        output_IntVal( digits );
//        output_IntVal( retVal );

        int src = digits.Length - 1;
        int dst = retVal.Length - 1;
        
        for (  ; src >= 0; src--, dst--) {
            retVal[dst] += digits[src];
            
            if ( retVal[dst] == 10 ) {
                retVal[dst - 1]++;
                retVal[dst] = 0;
            }
        }

//        output_IntVal( digits );
//        output_IntVal( retVal );

        return retVal;
    }
    
    private bool Check_Carry(int[] digits)
    {
        for (int i = 0; i < digits.Length; ++i) {
            if (digits[i] == 9)
                continue;
            else
                return false;
        }
        
        return true;
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
        string flds = args.Replace("[", "").Replace("]", "").Trim();
        int[] digits = str_to_int_array(flds);
        Console.WriteLine("digits = " + output_int_array(digits));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();

        sw.Start();

        int[] result = PlusOne( digits );

        sw.Stop();

        Console.WriteLine("result = " + output_int_array(result));
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
