using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public IList<int> PowerfulIntegers(int x, int y, int bound)
    {
        var result = new HashSet<int>();

        for (int a = 1; a < bound; a *=x )
        {
            for(int b = 1; a + b <= bound; b *= y)
            {
                result.Add(a + b);

                if(y == 1)
                {
                    break;
                }
            }

            if (x == 1)
                break;
        }

        return new List<int>(result);         
    }

    /*
    public IList<int> PowerfulIntegers(int x, int y, int bound)
    {
        IList<int> results = new List<int>();
        IList<int, int> stack = new List<int, int>();

        while (stack.Count > 0)
        {
            i = stack[stack.Count - 1][0];
            j = stack[stack.Count - 1][1];
            stack.Remove();
            t = x ** i + y ** j;
            if (t <= bound)
            {
                s.Add(t);
                if (x > 1)
                    stack.Add(i + 1, j);
                if (y > 1)
                    stack.Add(i, j + 1);
            }
        }
        return results;
    }
    */

    public string output_IList_array(IList<int> datas)
    {
        if (datas.Count <= 0)
            return "";

        string resultStr = datas[0].ToString();
        for (int i = 1; i < datas.Count; ++i)
        {
            resultStr += "," + datas[i].ToString();
        }

        return resultStr;
    }

    public void Main(string args)
    {
        string[] flds = args.Replace("[","").Replace("]","").Trim().Split(',');
        int x = 0, y = 0, bound = 0;

        try
        {
            x = int.Parse(flds[0]);
            y = int.Parse(flds[1]);
            bound = int.Parse(flds[2]);
        }
        catch (Exception e)
        {
            Console.WriteLine(e.Message);
            Environment.Exit(-1);
        }

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        IList<int> results = PowerfulIntegers(x, y, bound);
        Console.WriteLine("result = " + output_IList_array(results));

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
