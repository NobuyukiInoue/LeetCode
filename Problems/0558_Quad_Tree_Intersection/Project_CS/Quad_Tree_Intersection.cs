using System;
using System.Collections.Generic;
using System.Linq;

// Definition for a QuadTree node.
public class Node {
    public bool val;
    public bool isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;

    public Node(){}
    public Node(bool _val,bool _isLeaf,Node _topLeft,Node _topRight,Node _bottomLeft,Node _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
}

public class Solution {
    public Node Construct(int[][] grid)
    {
        
    }

    public int[][] str_to_int_array(string[] flds)
        {
            if (flds.Length <= 0)
                return null;

            int[][] grid = new int[flds.Length][];
            string[] temp;

            for (int i = 0; i < flds.Length; ++i)
            {
                temp = flds[i].Split(',');
                grid[i] = new int[temp.Length];
                for (int j = 0; j < temp.Length; ++j)
                {
                    grid[i][j] = int.Parse(temp[j]);
                }
            }

        return grid;
    }

    public string output_grid(int[][] grid)
    {
        if (grid.Length <= 0)
            return "";

        string resultStr = "";
        for (int i = 0; i < grid.Length; ++i)
        {
            if (i == 0)
                resultStr += "[";
            else
                resultStr += ",[";

            for (int j = 0; j < grid[i].Length; ++ j)
            {
                if (j == 0)
                    resultStr += "[" + grid[i][j].ToString();
                else
                    resultStr += "," + grid[i][j].ToString();
            }
            resultStr += "]";
        }

        return resultStr + "]";
    }

    public void Main(string args)
    {
        string temp = args.Replace("[[","").Replace("]]","").Trim();
        string[] flds = temp.Split(new string[] {"],["}, StringSplitOptions.None);
        int[][] grid = str_to_int_array(flds);

        Console.WriteLine("grid = " + output_grid(grid));
        
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        Node node = Construct(grid);
        //Console.WriteLine("result = " + node.ToString());

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
        /*
        Console.Write("Hit Any Key");
        Console.Read();
        */
    }
}
