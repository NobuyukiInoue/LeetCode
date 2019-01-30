using System;

public class Operate_ListNode
{
    public ListNode set_nodes(int[] nums)
    {
        return set_nodes(nums, 0);
    }

    public ListNode set_nodes(int[] nums, int index)
    {
        if (nums == null)
            return null;

        if (index >= nums.Length)
            return null;
        
        ListNode node = new ListNode(nums[index]);
        node.next = set_nodes(nums, index + 1);

        return node;
    }

    public string output_nodes(ListNode node)
    {
        if (node == null)
            return "";

        string resultStr = node.val.ToString();

        if (node.next != null)
            resultStr += " -> " + output_nodes(node.next);

        return (resultStr);
    }
}
