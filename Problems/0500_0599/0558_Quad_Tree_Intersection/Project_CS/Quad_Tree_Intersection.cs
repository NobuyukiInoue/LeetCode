using System;
using System.Collections.Generic;
using System.IO;
using System.Runtime.Serialization.Json;
using System.Text;

// Definition for a QuadTree node.
public class Node {
    public bool val;
    public bool isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;

    public Node(){}
    public Node(bool _val, bool _isLeaf, Node _topLeft, Node _topRight, Node _bottomLeft, Node _bottomRight)
    {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
}

public class Solution
{
    public Node Intersect(Node quadTree1, Node quadTree2)
    {
        if (quadTree1.isLeaf && quadTree1.val) return quadTree1;
        if (quadTree2.isLeaf && quadTree2.val) return quadTree2;
        if (quadTree1.isLeaf && !quadTree1.val) return quadTree2;
        if (quadTree2.isLeaf && !quadTree2.val) return quadTree1;     
        
        Node tl = Intersect(quadTree1.topLeft, quadTree2.topLeft);
        Node tr = Intersect(quadTree1.topRight, quadTree2.topRight);
        Node bl = Intersect(quadTree1.bottomLeft, quadTree2.bottomLeft);
        Node br = Intersect(quadTree1.bottomRight, quadTree2.bottomRight);
        
        if(tl.val == tr.val && tl.val == bl.val && tl.val == br.val && tl.isLeaf && tr.isLeaf && bl.isLeaf && br.isLeaf)
            return new Node(tl.val, true, null, null, null, null);
        else         
            return new Node(false, false, tl, tr, bl, br);
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

    private Node File_to_Node(string fileName)
    {
        Console.WriteLine("readfile = " + fileName);

        FileStream fs = new FileStream(fileName, FileMode.Open);
        StreamReader sr = new StreamReader(fs);
        string json_text = sr.ReadToEnd();

        Console.WriteLine("read json = " + json_text);

        return json_text_to_Node(json_text);
    }

    private Node json_text_to_Node(string json_text)
    {
        var ms = new MemoryStream(Encoding.UTF8.GetBytes(json_text));
        var serializer = new DataContractJsonSerializer(typeof(Node));
        var data = (Node)serializer.ReadObject(ms);

        Node node = new Node(data.val, data.isLeaf, data.topLeft, data.topRight, data.bottomLeft, data.bottomRight);
        return node;
    }

    private string output_all_TreeNode(Node node)
    {
        int id = 1;
        return "{" + output_TreeNode(node, id).Replace("True", "true").Replace("False", "false") + "}";
    }

    private string output_TreeNode(Node node, int id)
    {
        if (node == null)
            return ":null";

        string resultStr = "\"$id\":\"" + id.ToString() + "\"";

        resultStr += ",\"bottomLeft\":";
        if (node.bottomLeft == null)
            resultStr += "null";
        else
            resultStr += "{" + output_TreeNode(node.bottomLeft, id + 3) + "}";

        resultStr += ",\"bottomRight\":";
        if (node.bottomRight == null)
            resultStr += "null";
        else
            resultStr += "{" + output_TreeNode(node.bottomRight, id + 4) +"}";

        resultStr += ",\"isLeaf\":" + node.isLeaf.ToString();

        resultStr += ",\"topLeft\":";
        if (node.topLeft == null)
            resultStr += "null";
        else
            resultStr += "{" + output_TreeNode(node.topLeft, id + 1) + "}";

        resultStr += ",\"topRight\":";
        if (node.topRight == null)
            resultStr += "null";
        else
            resultStr += "{" + output_TreeNode(node.topRight, id + 2) +"}";

        resultStr += ",\"val\":" + node.val.ToString();

        return resultStr;
    }

    public void Main(string args)
    {
    	string[] filenames = args.Replace("\"", "").Replace("[[","").Replace("]]","").Trim().Split(new string[] {"],["}, StringSplitOptions.None);

        Node quadTree1 = File_to_Node(filenames[0]);
        Node quadTree2 = File_to_Node(filenames[1]);

        Console.WriteLine("quadTree1 = " + output_all_TreeNode(quadTree1) + "\n");
        Console.WriteLine("quadTree2 = " + output_all_TreeNode(quadTree2) + "\n");

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        Node result = Intersect(quadTree1, quadTree2);

        sw.Stop();

        Console.WriteLine("result = " + output_all_TreeNode(result) + "\n");
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
