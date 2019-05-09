using System;
using System.Linq;

public class Solution
{
    public string AddStrings(string num1, string num2)
    {
        int results_length;
        if (num1.Length > num2.Length)
            results_length = num1.Length + 1;
        else
            results_length = num2.Length + 1;

        char[] results = Enumerable.Repeat<char>('0', results_length).ToArray();
        int i = num1.Length - 1;
        int j = num2.Length - 1;
        int k = results.Length - 1;

        while (i >= 0 || j >= 0)
        {
            int sum = 0;
            if (i >= 0)
                sum += (int)(num1[i]) - 0x30;
                i--;
            if (j >= 0)
                sum += (int)(num2[j]) - 0x30;
                j--;
            if (k >= 0)
                sum += (int)(results[k]) - 0x30;

            results[k] = (char)(sum % 10 + 0x30);

            if (k > 0)
                results[k - 1] = (char)(sum / 10 + 0x30);
            k--;
        }

        string resultsStr = new string(results);
        if (resultsStr[0] == '0')
            return resultsStr.Substring(1);
        else
            return resultsStr;
    }

    public void Main(string args)
    {
        string[] var_args = args.Replace("\"","").Replace("[","").Replace("]","").Trim().Split(',');
        string num1 = var_args[0];
        string num2 = var_args[1];
        Console.WriteLine("num1 = " + num1 + "\nnum2 = " + num2);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        string result = AddStrings(num1, num2);
        Console.WriteLine("result = " + result);
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
