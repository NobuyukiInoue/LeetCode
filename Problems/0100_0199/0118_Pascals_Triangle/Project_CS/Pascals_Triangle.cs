using System;
using System.Collections.Generic;

public class Solution {
/*
    public IList<IList<int>> Generate(int numRows) {
        IList<IList<int>> result = new List<IList<int>>();
        for(int i = 1; i <= numRows; i++){
            IList<int> singleLine = new List<int>();
            for(int j = 1; j <= i; j++)
                singleLine.Add(j == 1 || j == i ? 1 : result[i - 2][j - 2] + result[i - 2][j - 1]);
            result.Add(singleLine);
        }
        return result;
    }
*/
    public IList<IList<int>> Generate(int numRows)
    {
        int i, j;
        IList<IList<int>> rows = new List<IList<int>>();

        IList<int>[] tempList = new List<int>[numRows];
        for (i = 0; i < numRows; i++)
        {
            tempList[i] = new List<int>();
        }

        if (numRows <= 0)
            return rows;

        tempList[0].Add(1);
        rows.Add(tempList[0]);
        if (numRows <= 1)
            return rows;

        tempList[1].Add(1);
        tempList[1].Add(1);
        rows.Add(tempList[1]);

        for (i = 2; i < numRows; i++) {
            tempList[i].Add(1);
            for (j = 1; j < i; j++) {
                tempList[i].Add(rows[i - 1][j] + rows[i - 1][j - 1]);
            }
            tempList[i].Add(1);
            rows.Add(tempList[i]);
        }
        return rows;
    }

    public string output_IList_array(IList<IList<int>> flds)
    {
        string results = "";
        if (flds.Count <= 0)
            return results;
        
        results = "[";
        for (int i = 0; i < flds.Count; ++i)
        {
            results += "[" + flds[i][0].ToString();
            for (int n = 1; n < flds[i].Count; ++n)
                results += ", " + flds[i][n].ToString();
            if (i < flds.Count - 1)
                results += "],";
            else
                results += "]";
        }

        return results + "]";
    }

    public void Main(string args)
    {
        Console.WriteLine("args = " + args);
        String flds = args.Replace("[", "").Replace("]", "");
        int numRows = int.Parse(flds);
        Console.WriteLine("numRows = " + numRows.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        IList<IList<int>> result = Generate(numRows);
        Console.WriteLine("result = " + output_IList_array(result));

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
