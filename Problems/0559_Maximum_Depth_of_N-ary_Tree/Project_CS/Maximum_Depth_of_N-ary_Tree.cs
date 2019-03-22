using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.Serialization.Json;
using System.Text;

public class Node
{
    public int val;
    public IList<Node> children;

    public Node()
    {
    }
    public Node(int _val, IList<Node> _children)
    {
        val = _val;
        children = _children;
    }
}

public class Solution
{
    public int MaxDepth(Node root)
    {
        if (root == null)
            return 0;
        
        if (root.children == null)
            return 1;

        var depths = new List<int>();
        foreach (Node child in root.children)
            depths.Add(MaxDepth(child));
        
        if (depths.Count > 0)
            return depths.Max() + 1;
        else
            return 1;
    }
    
    public Node set_sample_node()
    {
        IList<Node> n1_list = new List<Node>();
        n1_list.Add(new Node(5, null));
        n1_list.Add(new Node(6, null));

        IList<Node> n0_list = new List<Node>();
        n0_list.Add(new Node(3, n1_list));
        n0_list.Add(new Node(2, null));
        n0_list.Add(new Node(4, null));

        Node node = new Node(1, n0_list);

        return node;
    }

    public string output_node(Node node)
    {
        if (node == null)
            return "";

        resultStr = new List<string>();

        resultStr.Add(node.val.ToString());
        set_output_node(node, 1);

        if (resultStr.Count <= 0)
            return "";

        string result = "[\n";
        for (int i = 0; i < resultStr.Count; ++i)
        {
            if (resultStr[i] == "")
                break;

            if (i < resultStr.Count - 1)
                result += "\t[" + resultStr[i] + "],\n";
            else
                result += "\t[" + resultStr[i] + "]\n";
        }
        result += "]";

        resultStr.Clear();
        return result;
    }

    List<string> resultStr;

    public void set_output_node(Node node, int n)
    {
        if (node == null)
            return;

        if (node.children == null)
            return;

        string tempStr = "";
        for (int i = 0; i < node.children.Count; ++i)
        {
            if (i == 0)
                tempStr += node.children[i].val;
            else
                tempStr += "," + node.children[i].val;
        }

        if (resultStr.Count <= n)
                resultStr.Add(tempStr);
        else
            resultStr[n] += tempStr;

        for (int i = 0; i < node.children.Count; ++i)
        {
            set_output_node(node.children[i], n + 1);
        }
    }
    private Node json_text_to_Node(string json_text)
    {
        var ms = new MemoryStream(Encoding.UTF8.GetBytes(json_text));
        var serializer = new DataContractJsonSerializer(typeof(Node));
        var data = (Node)serializer.ReadObject(ms);

        Node node = new Node(data.val, null);
        node.children = data.children;

        return node;
    }

    public void Main(string args)
    {
        Node root = json_text_to_Node(args.Trim());
    //  Node root = set_sample_node();

        Console.WriteLine(output_node(root) + "\n");

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = MaxDepth(root);

        sw.Stop();
        Console.WriteLine("result = " + result.ToString());
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
