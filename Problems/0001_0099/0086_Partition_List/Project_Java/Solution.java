public class Solution {
    public ListNode partition(ListNode head, int x) {
        // 0ms
        ListNode cur = head;
        
        ListNode smaller_sentinel = new ListNode(0);
        ListNode smaller_cur = smaller_sentinel;
        ListNode larger_sentinel = new ListNode(0);
        ListNode larger_cur = larger_sentinel;

        while (cur != null) {
            if (cur.val < x) {
                    smaller_cur.next = cur;
                    smaller_cur = smaller_cur.next;
                
            } else {
                    larger_cur.next = cur;
                    larger_cur = larger_cur.next;
            }
            cur = cur.next;
        }

        larger_cur.next = null;
        smaller_cur.next = larger_sentinel.next;
        return smaller_sentinel.next;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib mc = new Mylib();
        int[] nums = mc.str_to_int_array(flds[0]);

        System.out.println("nums = " + mc.output_int_array(nums));

        Operate_ListNode ope = new Operate_ListNode();
        ListNode head = ope.set_ListNode(nums);
        System.out.println("head = " + ope.output_ListNode(head));

        int x = Integer.parseInt(flds[1]);
        long start = System.currentTimeMillis();

        ListNode result = partition(head, x);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope.output_ListNode(result));
        System.out.println((end - start)  + "ms\n");
    }
}
