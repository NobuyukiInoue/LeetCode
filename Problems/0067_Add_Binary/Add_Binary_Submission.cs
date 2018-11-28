using System;
using System.Text;

public class Solution
{
    public string AddBinary(string a, string b)
    {
        int i, max_len;
        char val_a, val_b, val_c;
        string result;

        if (a.Length >= b.Length)
            max_len = a.Length + 1;
        else
            max_len = b.Length + 1;

        char[] c = new char[max_len];
        for ( i = 0; i < max_len; ++i ) {
            c[i] = '0';
        }

        i = 1;
        while (i <= max_len) {
            if (i > a.Length)
                val_a = '0';
            else
                val_a = a[a.Length - i];

            if (i > b.Length)
                val_b = '0';
            else
                val_b = b[b.Length - i];

            if (i > c.Length)
                val_c = '0';
            else
                val_c = c[c.Length - i];
            
            switch (val_a + val_b + val_c) {
            case 0x90:
                result = "00";
                break;
            case 0x91:
                result = "01";
                break;
            case 0x92:
                result = "10";
                break;
            case 0x93:
                result = "11";
                break;
            default:
                result = "00";
                break;
            }

            if ( c.Length - i - 1 >= 0 )
                c[c.Length - i - 1] = result[0];

            c[c.Length - i] = result[1];
            ++i;
        }

        string result_str = "";
        
        if (c[0] == '1')
            result_str = "1";

        for ( i = 1; i < c.Length; i++ )
        {
            result_str += c[i];
        }

        return(result_str);
    }

    private long ToDecimal(string workStr)
    {
        long val = 0, n = 1;
        
        for (int i = workStr.Length - 1; i >= 0; --i) {
            val += (workStr[i] - '0')*n;
            n *= 2;
        }
        
        Console.WriteLine("val = " + val.ToString() );
        return (val);
    }

    private void output_Str(string[] data)
    {
        for (int i = 0; i < data.Length; i++) {
            Console.Write( " " + data[i] );
        }

        Console.WriteLine();
    }
    
    public void Main(string args)
    {
        Console.WriteLine("args = \"" + args + "\"");

        string[] data = args.Split(',');
        output_Str( data );

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();

        sw.Start();

        string str = AddBinary(data[0], data[1]);
        Console.WriteLine("Result(bin) = " + str + ", Result(dec) = " + ToDecimal(str) );
        
        sw.Stop();

        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
