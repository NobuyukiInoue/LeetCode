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

        Console.WriteLine("max_len = " + max_len.ToString() );
        Console.Write("c = ");
        char[] c = new char[max_len];
        for ( i = 0; i < max_len; ++i ) {
            c[i] = '0';
            Console.Write(c[i]);
        }
        Console.WriteLine();

        i = 1;
        while (i <= max_len) {

            if (i > a.Length)
                val_a = '0';
            else
                val_a = (char)a[a.Length - i];

            if (i > b.Length)
                val_b = '0';
            else
                val_b = (char)b[b.Length - i];

            if (i > c.Length)
                val_c = '0';
            else
                val_c = (char)c[c.Length - i];
            
        //    Console.WriteLine("[" + i.ToString() + "] ... a = " + val_a.ToString() + ", b = " + val_b.ToString() + ", c = " + val_c.ToString());
            result = binary_add(val_a, val_b, val_c);
        //    Console.WriteLine("Debug0...");

            if ( c.Length - i - 1 >= 0 )
                c[c.Length - i - 1] = result[0];

            c[c.Length - i] = result[1];
        //    Console.WriteLine("Debug1...");

        //    output_c(c);

            ++i;
        }

        string result_str = "";
        
        if (c[0] == '1')
            result_str = "1";

        for ( i = 1; i < c.Length; i++ )
        {
            result_str += c[i];
        }

    //    Console.WriteLine("result_str = " + result_str);
        return(result_str);
    }

    private void output_c(char[] c)
    {
        for (int i = 0; i < c.Length; i++) {
            Console.Write(c[i]);
        }
        Console.WriteLine();
    }

    private string binary_add(char a, char b, char c)
    {
        int sum = a - '0' + b - '0' + c;
        
        switch (sum) {
        case '0':
            return ("00");
        case '1':
            return ("01");
        case '2':
            return ("10");
        case '3':
            return ("11");
        default:
            return ("00");
        }
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
