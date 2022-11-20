public class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // 1ms
        ListNode dummy = new ListNode (0);
        ListNode head = dummy;
        while (true) {
            if (list1 == null) {
                dummy.next=list2;
                break;
            }
            if (list2 == null) {
                dummy.next = list1;
                break;
            }
            if (list1.val <= list2.val) {
                dummy.next=list1;
                list1=list1.next;
            } else {
                dummy.next = list2;
                list2 = list2.next;
            }
            dummy=dummy.next;
        }
        return head.next;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        OperateListNode ope = new OperateListNode();
        ListNode list1, list2;
        if (flds.length == 0) {
            list1 = list2 = null;
        } else {
            if (flds[0].equals("")) {
                list1 = null;
            } else {
                list1 = ope.createListNode(flds[0]);
            }
            if (flds[1].equals("")) {
                list2 = null;
            } else {
                list2 = ope.createListNode(flds[1]);
            }
        }
        System.out.println("list1 = " + ope.listNodeToString(list1));
        System.out.println("list2 = " + ope.listNodeToString(list2));

        long start = System.currentTimeMillis();

        ListNode result = mergeTwoLists(list1, list2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope.listNodeToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
