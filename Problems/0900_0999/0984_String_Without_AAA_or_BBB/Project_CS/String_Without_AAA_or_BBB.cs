using System;

public class Solution
{
    public string StrWithout3a3b(int A, int B)
    {
        string resultStr = "";

        while (A > B && B > 0)
        {
            resultStr += "aab";
            A -= 2;
            B--;
        }

        while (B > A && A > 0)
        {
            resultStr += "bba";
            B -= 2;
            A--;
        }

        if (A == 0 || B == 0)
            if (B == 0)
                resultStr += new string('a', A);
            else
                resultStr += new string('b', B);
        else if (resultStr.Length == 0 || resultStr[resultStr.Length - 1] == 'a')
        {
            // resultStr += new string("ba", A);
            for (int i = 0; i < A; ++i)
                resultStr += "ba";
        }
        else
        {
            // resultStr += new string("ab", A);
            for (int i = 0; i < B; ++i)
                resultStr += "ab";
        }

        return resultStr;
    }

    public void Main(string args)
    {
        string[] flds = args.Replace("[","").Replace("]","").Trim().Split(',');
        int A = int.Parse(flds[0]);
        int B = int.Parse(flds[1]);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        string result = StrWithout3a3b(A, B);
        Console.WriteLine("result = " + result);

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
