public class OperateListNode {
    public ListNode createListNode(String flds) {
        if (flds.length() == 0)
            return null;
        return createSubListNode(flds.split(","), 0);
    }

    public ListNode createSubListNode(String[] flds, int index) {
        if (flds == null)
            return null;

        if (index >= flds.length)
            return null;
        
        ListNode node = new ListNode(Integer.parseInt(flds[index]));
        node.next = createSubListNode(flds, index + 1);

        return node;
    }

    public String listNodeToString(ListNode node) {
        if (node == null)
            return "";

        String resultStr = Integer.toString(node.val);

        if (node.next != null)
            resultStr += " -> " + listNodeToString(node.next);

        return (resultStr);
    }
}
