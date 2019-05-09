public class Operate_ListNode
{
    public ListNode set_ListNode(int[] nums)
    {
        return set_ListNode(nums, 0);
    }

    public ListNode set_ListNode(int[] nums, int index)
    {
        if (nums == null)
            return null;

        if (index >= nums.length)
            return null;
        
        ListNode node = new ListNode(nums[index]);
        node.next = set_ListNode(nums, index + 1);

        return node;
    }

    public String output_ListNode(ListNode node)
    {
        if (node == null)
            return "";

        String resultStr = Integer.toString(node.val);

        if (node.next != null)
            resultStr += " -> " + output_ListNode(node.next);

        return (resultStr);
    }
}
