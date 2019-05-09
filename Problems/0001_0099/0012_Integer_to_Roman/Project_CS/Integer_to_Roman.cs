using System;
using System.Linq;
using System.Collections.Generic;
using System.Text;

public class Solution
{
    public List<(int number, string numeral)> Numerals = new List<(int value, string numeral)>
    {
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    };

    public string IntToRoman(int num) 
    {
        var sb = new StringBuilder();
        foreach(var entry in Numerals)
        {
            if ( num < entry.number)
            {
                continue;
            }
            
            int remain = num % entry.number;
            int count = num / entry.number;
            
            sb.Append(entry.numeral);
            for(int j = 1; j < count;j++)
            {
                sb.Append(entry.numeral);
            }
            
            num = remain;
        }

        return sb.ToString();
    }

    public void Main(string args)
    {
        int num = int.Parse(args.Replace("[","").Replace("]","").Trim());

        Console.WriteLine("num = " + num.ToString());
        
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        string result = IntToRoman(num);
        Console.WriteLine("result = " + result);
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
