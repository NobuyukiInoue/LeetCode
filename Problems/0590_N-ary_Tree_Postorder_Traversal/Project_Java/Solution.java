import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Solution {

    public List<Integer> postorder(Node root) {
        List<Integer> result = new LinkedList<>();
        Stack<Node> nodeStack = new Stack<>();
        if (root == null) {
            return result;
        }
        
        nodeStack.push(root);
        
        while (!nodeStack.isEmpty()) {
            Node nextNode = nodeStack.pop();
            result.add(0, nextNode.val);
            
            for (Node node : nextNode.children) {
                if (node != null) {
                    nodeStack.push(node);
                }
            }
        }
        return result;
    }

    public String List_array_to_String(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + Integer.toString(list.get(0));
        for (Integer i = 1; i < list.size(); i++) {
            resultStr += "," + Integer.toString(list.get(i));
        }

        return resultStr + "]";
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String json_text = args.trim().replace("$id", "val");
        ObjectMapper mapper = new ObjectMapper();
        Node root = null;

        try {
            root = mapper.readValue(json_text, Node.class);
        } catch (Exception ex) {
            System.out.println("\nmapper.readValue() Error.\n" + ex.getMessage());
            System.exit(1);
        }

        Operate_N_arr opn = new Operate_N_arr();
    //    Node root = opn.set_sample_node();
        System.out.println("root = " + opn.output_node(root));

        Mylib ml = new Mylib();

        long start = System.currentTimeMillis();

        List<Integer> result = postorder(root);

        long end = System.currentTimeMillis();

        System.out.println("result = " + List_array_to_String(result));
        System.out.println((end - start)  + "ms\n");
    }
}
