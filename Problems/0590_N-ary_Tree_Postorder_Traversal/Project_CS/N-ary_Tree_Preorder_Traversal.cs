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
    public IList<int> list = new List<int>();

    public IList<int> Preorder(Node root)
    {
        if (root == null)
            return list;

        list.Add(root.val);
        if (root.children == null)
            return list;

        foreach (var node in root.children) {
            Preorder(node);
        }

        return list;
    }

    /*
    public IList<int> Preorder(Node root)
    {
        IList<int> list = new List<int>();

        if (root == null)
            return list;

        list.Add(root.val);
        foreach (var node in root.children) {
            IList<int> temp_list = Preorder(node);
            for (int i = 0; i < temp_list.Count; i++)
            {
                list.Add(temp_list[i]);
            }
        }

        return list;
    }
    */
    
    private Node json_text_to_Node(string json_text)
    {
        var ms = new MemoryStream(Encoding.UTF8.GetBytes(json_text));
        var serializer = new DataContractJsonSerializer(typeof(Node));
        var data = (Node)serializer.ReadObject(ms);

        Node node = new Node(data.val, null);
        node.children = data.children;

        return node;
    }

    public String ListArray_to_String(IList<int> list)
    {
        if (list.Count <= 0)
            return "";

        String resultSTr = "[" + list[0];
        for (int i = 1; i < list.Count; i++)
        {
            resultSTr += "," + list[i];
        }

        return resultSTr + "]";
    }
    public void Main(string args)
    {
        Node root = json_text_to_Node(args.Trim());
        //Node root = set_sample_node();

        Operate_N_arr opa = new Operate_N_arr();
        Console.WriteLine(opa.output_node(root) + "\n");

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        IList<int> result = Preorder(root);

        sw.Stop();
        Console.WriteLine("reuslt = " + ListArray_to_String(result));
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
