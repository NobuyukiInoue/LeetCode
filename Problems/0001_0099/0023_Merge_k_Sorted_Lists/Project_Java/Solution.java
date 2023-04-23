public class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        // 1ms
        if (lists == null || lists.length == 0) {
            return null;
        }
        return mergeKListsHelper(lists, 0, lists.length - 1);
    }
    
    private ListNode mergeKListsHelper(ListNode[] lists, int start, int end) {
        if (start == end) {
            return lists[start];
        }
        if (start + 1 == end) {
            return merge(lists[start], lists[end]);
        }
        int mid = start + (end - start) / 2;
        ListNode left = mergeKListsHelper(lists, start, mid);
        ListNode right = mergeKListsHelper(lists, mid + 1, end);
        return merge(left, right);
    }
    
    private ListNode merge(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                curr.next = l1;
                l1 = l1.next;
            } else {
                curr.next = l2;
                l2 = l2.next;
            }
            curr = curr.next;
        }
        curr.next = (l1 != null) ? l1 : l2;
        return dummy.next;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        OperateListNode ope = new OperateListNode();
        ListNode lists[] = new ListNode[flds.length];
        for (int i = 0; i < flds.length; i++) {
            lists[i] = ope.createListNode(flds[i]);
            System.out.println("lists[" + i + "] = [" + ope.listNodeToString(lists[i]) + "]");
        }
        long start = System.currentTimeMillis();

        ListNode result = mergeKLists(lists);

        long end = System.currentTimeMillis();

        System.out.println("result = [" + ope.listNodeToString(result) + "]");
        System.out.println((end - start)  + "ms\n");
    }
}
