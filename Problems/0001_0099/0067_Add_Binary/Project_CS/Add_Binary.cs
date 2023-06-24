using System;
using System.Text;

public class Solution
{
    public string AddBinary(string a, string b)
    {
        // 72ms - 85ms 
        string ans = "";
        int carry = 0;
        int i = a.Length - 1;
        int j = b.Length - 1;
        while ((i >= 0) || (j >= 0) || carry != 0) {
            if (i >= 0) {
                carry += a[i--] - '0';
            }
            if (j >= 0) {
                carry += b[j--] - '0';
            }
            ans = (char)(carry % 2 + '0') + ans;
            carry /= 2;
        }
        return ans;
    }

    private long ToDecimal(string workStr)
    {
        long val = 0, n = 1;
        
        for (int i = workStr.Length - 1; i >= 0; --i) {
            val += (workStr[i] - '0')*n;
            n *= 2;
        }
        return (val);
    }
    
    public void Main(string args)
    {
        string arg_str = args.Replace("[[","").Replace("]]","").Replace("\"", "").Trim();
        string[] flds = arg_str.Split(new string[] {"],["}, StringSplitOptions.None);
        string a = flds[0];
        string b = flds[1];
        Console.WriteLine("a = " + ToDecimal(a).ToString());
        Console.WriteLine("b = " + ToDecimal(b).ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();

        sw.Start();

        string result = AddBinary(a, b);
        
        sw.Stop();

        Console.WriteLine("Result(bin) = \"" + result + "\", Result(dec) = " + ToDecimal(result) );
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
