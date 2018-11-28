using System;
using System.Text;

public class Solution
{
    public int[] PlusOne(int[] digits)
    {
        int retVal_Length = 0;

        for (int i = 0; i < digits.Length; ++i) {
            if (digits[i] == 9)
                continue;
            else
                retVal_Length = digits.Length;
        }
        
        if (retVal_Length == 0)
            retVal_Length = digits.Length + 1;

        int[] retVal = new int[retVal_Length];

        retVal[retVal_Length - 1] = 1;

        int src = digits.Length - 1;
        int dst = retVal.Length - 1;
        
        for (  ; src >= 0; src--, dst--) {
            retVal[dst] += digits[src];
            
            if ( retVal[dst] == 10 ) {
                retVal[dst - 1]++;
                retVal[dst] = 0;
            }
        }

        return retVal;
    }

    private void output_IntVal(int[] data)
    {
        for (int i = 0; i < data.Length; i++) {
            Console.Write( " " + data[i].ToString() );
        }

        Console.WriteLine();
    }
    
    public void Main(string args)
    {
        Console.WriteLine("args = \"" + args + "\"");

        string[] args_str = args.Split(',');
        int[] args_val = new int[args_str.Length];

        for (int i = 0; i < args_str.Length; i++) {
            args_val[i] = Int32.Parse(args_str[i]);
        }

        Console.Write("args_val = ");
        output_IntVal( args_val );

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();

        sw.Start();

        int[] ret = PlusOne( args_val );
        Console.Write("ret_val = ");
        output_IntVal( ret );

        sw.Stop();

        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
