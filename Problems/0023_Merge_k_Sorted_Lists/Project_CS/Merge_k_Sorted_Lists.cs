using System;

//Definition for singly-linked list.
public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int x) { val = x; }
}

public class Solution
{
    public ListNode MergeKLists(ListNode[] lists)
    {
        if (lists.Length < 1)
            return null;
        if (lists == null)
            return null;

        int none_count = 0;
        foreach (ListNode temp_list in lists)
        {
            if (temp_list == null)
                none_count++;
        }
        if (none_count == lists.Length)
            return null;

        ListNode root = null;
        ListNode node = null;

        foreach (ListNode target_list in lists)
        {
            ListNode work_list = target_list;

            while (work_list != null)
            {
                if (node == null)
                {
                    root = new ListNode(work_list.val);
                    node = root;
                }
                else
                {
                    node.next = new ListNode(work_list.val);
                    node = node.next;
                }

                work_list = work_list.next;
            }
        }

        return Sort_ListNode(root);
    }

    public ListNode Sort_ListNode(ListNode list)
    {
        ListNode root = list;
        ListNode target = null;
        int temp;

        ListNode work = root;
        while (work != null)
        {
            target = work.next;
            while (target != null)
            {
                if (work.val > target.val)
                {
                    temp = work.val;
                    work.val = target.val;
                    target.val = temp;
                }
                target = target.next;
            }
            work = work.next;
        }

        return root;
    }

    public int[] str_to_int_array(string s)
    {
        if (s.Length <= 0)
            return null;

        string[] flds = s.Split(',');
        int[] nums = new int[flds.Length];

        if (flds.Length <= 0)
            return nums;

        for (int i = 0; i < nums.Length; ++i)
        {
            nums[i] = int.Parse(flds[i]);
        }

        return nums;
    }

    public string output_int_array(int[] nums)
    {
        if (nums == null)
            return "";

        if (nums.Length <= 0)
            return "";

        string resultStr = "[" +  nums[0].ToString();
 
        for (int i = 1; i < nums.Length; ++i)
        {
            resultStr += "," + nums[i].ToString();
        }

        return resultStr + "]";
    }

    public void Main(string args)
    {
        string arg_str = args.Replace("[[","").Replace("]]","").Trim();
        string[] flds = arg_str.Split(new string[] {"],["}, StringSplitOptions.None);

        int[][] nums = new int[flds.Length][];
        for (int i = 0; i < nums.Length; ++i)
        {
            nums[i] = str_to_int_array(flds[i]);
            Console.WriteLine("nums[" + i.ToString() + "] = " + output_int_array(nums[i]));
        }

        Operate_ListNode ope = new Operate_ListNode();
        ListNode[] lists = new ListNode[nums.Length];

        for (int i = 0; i < nums.Length; ++i)
        {
            lists[i] = ope.set_ListNode(nums[i]);
            Console.WriteLine("lists[" + i.ToString() + "] = " + ope.output_ListNode(lists[i]));
        }

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        ListNode result = MergeKLists(lists);
        sw.Stop();

        Console.WriteLine("result = " + ope.output_ListNode(result));
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
