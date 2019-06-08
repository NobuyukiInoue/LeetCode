using System;
using System.Collections.Generic;

public class Solution {
    public IList<int> GetRow(int rowIndex)
    {
        int i, j;
        IList<IList<int>> rows = new List<IList<int>>();

        IList<int>[] tempList = new List<int>[rowIndex + 1];
        for (i = 0; i < rowIndex + 1; i++)
        {
            tempList[i] = new List<int>();
        }

        tempList[0].Add(1);
        rows.Add(tempList[0]);
        if (rowIndex <= 0)
            return rows[0];

        tempList[1].Add(1);
        tempList[1].Add(1);
        rows.Add(tempList[1]);

        for (i = 2; i < rowIndex + 1; i++) {
            tempList[i].Add(1);
            for (j = 1; j < i; j++) {
                tempList[i].Add(rows[i - 1][j] + rows[i - 1][j - 1]);
            }
            tempList[i].Add(1);
            rows.Add(tempList[i]);
        }
        return rows[rowIndex];
    }

    public string output_IList_int_array(IList<int> flds)
    {
        String results = "[" + flds[0].ToString();
        for (int n = 1; n < flds.Count; ++n)
            results += ", " + flds[n].ToString();

        return results + "]";
    }

    public void Main(string args)
    {
        Console.WriteLine("args = " + args);
        String flds = args.Replace("[", "").Replace("]", "");
        int rowIndex = int.Parse(flds);
        Console.WriteLine("rowIndex = " + rowIndex.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        IList<int> result = GetRow(rowIndex);
        Console.WriteLine("result = " + output_IList_int_array(result));

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
