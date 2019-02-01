public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
    {
        ListNode dummyHead = new ListNode(0);
        ListNode p = l1, q = l2, curr = dummyHead;
        int carry = 0;

        while (p != null || q != null)
        {
            int x = (p != null) ? p.val : 0;
            int y = (q != null) ? q.val : 0;
            int sum = carry + x + y;
            carry = sum / 10;
            curr.next = new ListNode(sum % 10);
            curr = curr.next;
            if (p != null)
                p = p.next;
            if (q != null)
                q = q.next;
        }

        if (carry > 0)
        {
            curr.next = new ListNode(carry);
        }

        return dummyHead.next;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib mc = new Mylib();
        int[] nums1 = mc.str_to_int_array(flds[0]);
        int[] nums2 = mc.str_to_int_array(flds[1]);

        System.out.println("nums1 = " + mc.output_int_array(nums1));
        System.out.println("nums2 = " + mc.output_int_array(nums2));

        Operate_ListNode ope = new Operate_ListNode();
        ListNode l1 = ope.set_ListNode(nums1);
        ListNode l2 = ope.set_ListNode(nums2);
        System.out.println("l1 = " + ope.output_ListNode(l1));
        System.out.println("l2 = " + ope.output_ListNode(l2));

        long start = System.currentTimeMillis();

        ListNode result = AddTwoNumbers(l1, l2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope.output_ListNode(result));
        System.out.println((end - start)  + "ms\n");
    }
}
