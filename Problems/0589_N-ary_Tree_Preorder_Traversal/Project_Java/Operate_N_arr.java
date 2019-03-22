import java.util.*;

public class Operate_N_arr {
    public Node set_sample_node()
    {
        List<Node> n1_list = new ArrayList<Node>();
        n1_list.add(new Node(5, null));
        n1_list.add(new Node(6, null));

        List<Node> n0_list = new ArrayList<Node>();
        n0_list.add(new Node(3, n1_list));
        n0_list.add(new Node(2, null));
        n0_list.add(new Node(4, null));

        Node node = new Node(1, n0_list);

        return node;
    }

    List<String> resultStr;

    public String output_node(Node node)
    {
        if (node == null)
            return "";

        resultStr = new ArrayList<String>();

        resultStr.add(Integer.toString(node.val));
        set_output_node(node, 1);

        if (resultStr.size() <= 0)
            return "";

        String result = "[\n";
        for (int i = 0; i < resultStr.size(); ++i)
        {
            if (resultStr.get(i).equals(""))
                break;

            if (i < resultStr.size() - 1)
                result += "\t[" + resultStr.get(i) + "],\n";
            else
                result += "\t[" + resultStr.get(i) + "]\n";
        }
        result += "]";

        resultStr.clear();
        return result;
    }

    public void set_output_node(Node node, int n)
    {
        if (node == null)
            return;

        if (node.children == null)
            return;

        String tempStr = "";
        for (int i = 0; i < node.children.size(); ++i)
        {
            if (i == 0)
                tempStr += Integer.toString(node.children.get(i).val);
            else
                tempStr += "," + Integer.toString(node.children.get(i).val);
        }

        if (resultStr.size() <= n)
                resultStr.add(tempStr);
        else
            resultStr.set(n, resultStr.get(n) + tempStr);

        for (int i = 0; i < node.children.size(); ++i)
        {
            set_output_node(node.children.get(i), n + 1);
        }
    }
}
