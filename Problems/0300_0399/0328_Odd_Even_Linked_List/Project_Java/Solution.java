public class Solution {
    public ListNode oddEvenList(ListNode head) {
        // 0ms
        if (head == null || head.next == null)
            return head;

        ListNode next_head = head.next;
        ListNode cursor = head;
        int count = 1;
        ListNode last_odd_node = null;

        while (cursor != null) {
            if (count % 2 == 1)
                last_odd_node = cursor;
            ListNode temp_next = cursor.next;
            if (cursor.next != null)
                cursor.next = cursor.next.next;
            cursor = temp_next;
            count++;
        }

        last_odd_node.next = next_head;

        return head;       
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringTointArray(flds);

        System.out.println("nums = " + ml.intArrayToString(nums));

        Operate_ListNode ope = new Operate_ListNode();
        ListNode head = ope.set_ListNode(nums);
        System.out.println("head = " + ope.output_ListNode(head));

        long start = System.currentTimeMillis();

        ListNode result = oddEvenList(head);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope.output_ListNode(result));
        System.out.println((end - start)  + "ms\n");
    }
}
