using System;
using System.Collections.Generic;

public class Solution {
    public IList<string> ReadBinaryWatch(int num)
    {
        IList<string> res = new List<string>();
        IList<int> hour, min;
        int j;

        for (int i = 0; i < num + 1; ++i) {
            j = num - i;
            if (i >= 4 || j >= 6)
                continue;
            hour = Helper(4, i);
            min = Helper(6, j);
            hour = Shape(hour, true, false);
            min = Shape(min, false, true);

            foreach (int m in hour) {
                foreach (int n in min) {
                    if (n.ToString().Length != 1)
                        res.Add(m + ":" + n);
                    else
                        res.Add(m + ":0" + n);
                }
            } 
        }

        return res;
    }

    public IList<int> Shape(IList<int> arr, bool isHour, bool isMin)
    {
        IList<int> a = new List<int>();

        if (isHour) {
            for (int i = 0; i < arr.Count; ++i) {
                if (i < 12)
                    a.Add(i);
            }
        }

        if (isMin) {
            for (int i = 0; i < arr.Count; ++i) {
                if (i < 60)
                    a.Add(i);
            }
        }

        return a;
    }

    public IList<int> Helper(int n, int m)
    {
        IList<int> res = new List<int>();

        Backtracking(n, m, 0, 0, res);

        return res;
    }

    public void Backtracking(int n, int m, int pos, int sum, IList<int> res)
    {
        if (m == 0) {
            res.Add(sum);
            return;
        }

        if (pos == n)
            return;

        for (int i = pos; i < n; ++i) {
            Backtracking(n, m - 1, pos + 1, sum + (int)Math.Pow(2, n - pos - 1), res);
            Backtracking(n, m, pos + 1, sum, res);
        //    return;
        }

        return;

        /*
        if (pos < n) {
            Backtracking(n, m - 1, pos + 1, sum + (int)Math.Pow(2, n - pos - 1), res);
            Backtracking(n, m, pos + 1, sum, res);
            return;
        }
        */
    }

    public string Output_IList(IList<string> arr)
    {
        if (arr.Count < 1)
            return "";

        string resultStr = arr[0];
        for (int i = 0; i < arr.Count; ++i)
            resultStr += ", " + arr[i];
        
        return resultStr;
    }

    public void Main(string args)
    {
        int num = int.Parse(args);

        Console.WriteLine("num = " + num.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();
        
        IList<string> result = ReadBinaryWatch(num);

        Console.WriteLine("result = " + Output_IList(result));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
