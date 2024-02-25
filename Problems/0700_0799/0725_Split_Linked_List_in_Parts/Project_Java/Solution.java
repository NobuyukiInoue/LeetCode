import java.util.ArrayList;
import java.util.List;

public class Solution {
    public ListNode[] splitListToParts(ListNode head, int k) {
        // 0ms
        int length = 0;
        ListNode node = head;
        while (node != null) {
            node = node.next;
            length++;
        }
        node = head;
        int part_size = length/k, extra = length%k;
        ListNode[] ans = new ListNode[k];
        for (int i = 0; i < k; i++) {
            ans[i] = node;
            int current_part_size = extra > 0? part_size + 1: part_size;
            extra--;
            for (int j = 0; j < current_part_size - 1; j++) {
                node = node.next;
            }
            if (node != null) {
                ListNode temp = node.next;
                node.next = null;
                node = temp;
            }
        }
        return ans;
    }

    private String list_ListNodeToString(ListNode[] nodes) {
        OperateListNode ope = new OperateListNode();
        List<String> arr = new ArrayList<>();
        for (ListNode lst : nodes) {
            arr.add("[" + ope.listNodeToString(lst) + "]");
        }
        Mylib ml = new Mylib();
        return ml.listStringArrayToString(arr);
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        OperateListNode ope = new OperateListNode();
        ListNode head = ope.createListNode(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("head = " + ope.listNodeToString(head) + ", k = " + k);

        long start = System.currentTimeMillis();

        ListNode[] result = splitListToParts(head, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + list_ListNodeToString(result));
        System.out.println("]");
        System.out.println((end - start)  + "ms\n");
    }
}
