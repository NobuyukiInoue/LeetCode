using System;
using System.Collections.Generic;

namespace _0429_N_ary_node_Level_Order_Traversal
{
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
        public IList<IList<int>> LevelOrder(Node root)
        {
            IList<IList<int>> llist = new List<IList<int>>();

            if (root == null)
                return llist;

            IList<int> n0 = new List<int>();
            n0.Add(root.val);
            llist.Add(n0);

            for (int i = 0; i < root.children.Count; ++i)
            {
                nextOrder(root.children[i], llist, 1);
            }

            return llist;
        }

        public void nextOrder(Node node, IList<IList<int>> llist, int n)
        {
            if (node == null)
                return;

            if (llist.Count > n)
                llist[n].Add(node.val);
            else
            {
                IList<int> curr_list = new List<int>();
                curr_list.Add(node.val);
                llist.Add(curr_list);
            }

            if (node.children == null)
                return;

            for (int i = 0; i < node.children.Count; ++i)
            {
                nextOrder(node.children[i], llist, n + 1);
            }
        }

        public string outputOrder(IList<IList<int>> llist)
        {
            string resultStr = "";

            for (int i = 0; i < llist.Count; ++i)
            {
                resultStr += "[";
                for (int j = 0; j < llist[i].Count; ++j)
                {
                    if (j < llist[i].Count - 1)
                        resultStr += llist[i][j].ToString() + ",";
                    else
                        resultStr += llist[i][j].ToString();
                }
                resultStr += "]\n";
            }

            return resultStr;
        }

        public Node set_node()
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

            resultStr.Add(node.val.ToString());
            set_output_node(node, 1);

            if (resultStr.Count <= 0)
                return "";

            string result = "[\n";
            for (int i = 0; i < resultStr.Count; ++i)
            {
                if (i < resultStr.Count - 1)
                    result += "\t[" + resultStr[i] + "],\n";
                else
                    result += "\t[" + resultStr[i] + "]\n";
            }
            result += "]";

            return result;
        }

        List<string> resultStr = new List<string>();

        public void set_output_node(Node node, int n)
        {
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

        public void Main()
        {
            Node node = set_node();
            Console.WriteLine(output_node(node) + "\n");

            IList<IList<int>> llist = LevelOrder(node);
            Console.WriteLine(outputOrder(llist));
        }
    }

    public class Program
    {
        static void Main(string[] args)
        {
            Solution sl = new Solution();
            sl.Main();
        }
    }
}
