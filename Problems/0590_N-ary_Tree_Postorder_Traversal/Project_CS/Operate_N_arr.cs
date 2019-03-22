using System.Collections.Generic;

public class Operate_N_arr
{
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
}
