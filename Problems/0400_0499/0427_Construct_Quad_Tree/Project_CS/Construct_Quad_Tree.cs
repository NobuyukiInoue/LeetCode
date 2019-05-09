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
}

public class Solution {
    public Node Construct(int[][] grid)
    {
        return Construct(grid, 0, 0, grid.Length - 1, grid.Length - 1);
    }

    private Node Construct(int[][] grid, int iStart, int jStart, int iEnd, int jEnd)
    {
        if (iEnd == iStart)
        {
            Node nE = new Node();
            nE.isLeaf = true;
            nE.val = grid[iStart][jStart] == 1;
            return nE;
        }

        int mi = (iStart + iEnd) / 2;
        int mj = (jStart + jEnd) / 2;

        Node n = new Node();
        n.topLeft = Construct(grid, iStart, jStart, mi, mj);
        n.topRight = Construct(grid, iStart, mj + 1, mi, jEnd);
        n.bottomRight = Construct(grid, mi + 1, mj + 1, iEnd, jEnd);
        n.bottomLeft = Construct(grid, mi + 1, jStart, iEnd, mj);

        if (n.topLeft.isLeaf 
            && n.topLeft.isLeaf == n.topRight.isLeaf
            && n.bottomLeft.isLeaf == n.bottomRight.isLeaf
            && n.topLeft.isLeaf == n.bottomRight.isLeaf
            && n.topLeft.val == n.topRight.val
            && n.bottomLeft.val == n.bottomRight.val
            && n.topLeft.val == n.bottomRight.val)
            {
                n.isLeaf = true;
                n.val = n.topLeft.val;
                n.topLeft = n.topRight = n.bottomLeft = n.bottomRight = null;
            }
            return n;
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
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
        /*
        Console.Write("Hit Any Key");
        Console.Read();
        */
    }
}
